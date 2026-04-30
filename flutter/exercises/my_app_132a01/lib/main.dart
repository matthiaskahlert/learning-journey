/* 
Entwickle eine Flutter-App, die folgende Funktionen umfasst:

a) Erstelle eine Startseite mit einer Navigationsleiste, die Links zu drei weiteren Seiten enthält: "Kamera", "Einstellungen" und "Dateien".

b) Auf der "Kamera"-Seite soll der Nutzer Fotos aufnehmen können. Verwende das camera-Plugin, um Zugriff auf die Kamerafunktion des Geräts zu erhalten. Stelle sicher, dass die App die notwendigen Berechtigungen anfordert.

c) In den "Einstellungen" sollen Nutzer die Möglichkeit haben, ihre Präferenzen (z.B. Auflösung der Kamera) zu speichern. Verwende Shared Preferences, um diese Einstellungen zu speichern und bei einem Neustart der App wieder zu laden.

d) Auf der "Dateien"-Seite soll der Nutzer Zugriff auf gespeicherte Fotos erhalten. Implementiere eine Funktion zum Lesen und Anzeigen von Bildern aus dem Dateisystem des Geräts.

e) Füge eine Funktion hinzu, um Fotos und Texte über eine HTTP-POST-Anfrage an einen Server zu senden. Simuliere die Serverantwort in der App, ohne einen echten Server zu verwenden.
 */

import 'dart:convert';
import 'dart:io';

import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart' as path;
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter/foundation.dart' show kIsWeb;

class AppImageStore {
  static final List<String> _webImagePaths = <String>[];

  static List<String> get webImagePaths =>
      List<String>.unmodifiable(_webImagePaths);

  static void addWebImage(String imagePath) {
    _webImagePaths.insert(0, imagePath);
  }
}

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  List<CameraDescription> cameras = <CameraDescription>[];
  try {
    cameras = await availableCameras();
  } catch (_) {
    cameras = <CameraDescription>[];
  }

  runApp(MyApp(cameras: cameras));
}

class MyApp extends StatelessWidget {
  final List<CameraDescription> cameras;

  const MyApp({super.key, this.cameras = const <CameraDescription>[]});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Kamera App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomePage(cameras: cameras),
    );
  }
}

class HomePage extends StatefulWidget {
  final List<CameraDescription> cameras;

  const HomePage({super.key, required this.cameras});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;
  late final List<Widget> _pages;

  @override
  void initState() {
    super.initState();
    _pages = <Widget>[
      CameraPage(cameras: widget.cameras),
      const SettingsPage(),
      const FilesPage(),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (int index) {
          setState(() {
            _selectedIndex = index;
          });
        },
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.camera_alt),
            label: 'Kamera',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Einstellungen',
          ),
          BottomNavigationBarItem(icon: Icon(Icons.folder), label: 'Dateien'),
        ],
      ),
    );
  }
}

class CameraPage extends StatefulWidget {
  final List<CameraDescription> cameras;

  const CameraPage({super.key, required this.cameras});

  @override
  State<CameraPage> createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  CameraController? _controller;
  Future<void>? _initializeControllerFuture;
  ResolutionPreset _resolution = ResolutionPreset.medium;

  @override
  void initState() {
    super.initState();
    _loadSettingsAndInitCamera();
  }

  Future<void> _loadSettingsAndInitCamera() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    final String resolution = prefs.getString('resolution') ?? 'medium';
    _resolution = _getResolutionPreset(resolution);

    if (widget.cameras.isEmpty) {
      if (mounted) {
        setState(() {
          _initializeControllerFuture = null;
        });
      }
      return;
    }

    final CameraController controller = CameraController(
      widget.cameras.first,
      _resolution,
      enableAudio: false,
    );

    final Future<void> initFuture = controller.initialize();

    if (!mounted) {
      await controller.dispose();
      return;
    }

    setState(() {
      _controller = controller;
      _initializeControllerFuture = initFuture;
    });
  }

  ResolutionPreset _getResolutionPreset(String resolution) {
    switch (resolution) {
      case 'low':
        return ResolutionPreset.low;
      case 'high':
        return ResolutionPreset.high;
      case 'veryHigh':
        return ResolutionPreset.veryHigh;
      default:
        return ResolutionPreset.medium;
    }
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final CameraController? controller = _controller;
    final Future<void>? initFuture = _initializeControllerFuture;

    return Scaffold(
      appBar: AppBar(title: const Text('Kamera')),
      body: widget.cameras.isEmpty
          ? const Center(child: Text('Keine Kamera verfugbar'))
          : initFuture == null || controller == null
          ? const Center(child: CircularProgressIndicator())
          : FutureBuilder<void>(
              future: initFuture,
              builder: (BuildContext context, AsyncSnapshot<void> snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  return Column(
                    children: <Widget>[
                      Expanded(child: CameraPreview(controller)),
                      Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: ElevatedButton(
                          onPressed: () => _takePicture(),
                          child: const Text('Foto aufnehmen'),
                        ),
                      ),
                    ],
                  );
                }
                return const Center(child: CircularProgressIndicator());
              },
            ),
    );
  }

  Future<Directory> _getStorageDirectory() async {
    if (kIsWeb) {
      throw UnsupportedError(
        'Speichern von Dateien ist im Web nicht unterstützt.',
      );
    } else {
      return await getApplicationDocumentsDirectory();
    }
  }

  Future<void> _takePicture() async {
    final CameraController? controller = _controller;
    final Future<void>? initFuture = _initializeControllerFuture;

    if (controller == null || initFuture == null) {
      return;
    }

    try {
      await initFuture;

      final XFile image = await controller.takePicture();

      if (kIsWeb) {
        AppImageStore.addWebImage(image.path);
        if (!mounted) return;
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Foto im Browser gespeichert'),
            duration: Duration(seconds: 2),
          ),
        );
        return;
      }

      final Directory directory = await _getStorageDirectory();
      final String fileName = path.basename(image.path);
      final File savedImage = File(path.join(directory.path, fileName));

      await File(image.path).copy(savedImage.path);

      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Foto gespeichert: $fileName'),
          duration: const Duration(seconds: 2),
        ),
      );
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Fehler: $e'), backgroundColor: Colors.red),
      );
    }
  }
}

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  String _resolution = 'medium';

  @override
  void initState() {
    super.initState();
    _loadSettings();
  }

  Future<void> _loadSettings() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    if (!mounted) return;
    setState(() {
      _resolution = prefs.getString('resolution') ?? 'medium';
    });
  }

  Future<void> _saveSettings() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString('resolution', _resolution);

    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Einstellungen gespeichert'),
        duration: Duration(seconds: 2),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Einstellungen')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            const Text(
              'Kamera-Auflosung',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            DropdownButton<String>(
              value: _resolution,
              isExpanded: true,
              onChanged: (String? newValue) {
                if (newValue != null) {
                  setState(() {
                    _resolution = newValue;
                  });
                }
              },
              items: const <DropdownMenuItem<String>>[
                DropdownMenuItem<String>(value: 'low', child: Text('Niedrig')),
                DropdownMenuItem<String>(
                  value: 'medium',
                  child: Text('Mittel'),
                ),
                DropdownMenuItem<String>(value: 'high', child: Text('Hoch')),
                DropdownMenuItem<String>(
                  value: 'veryHigh',
                  child: Text('Sehr hoch'),
                ),
              ],
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: _saveSettings,
              child: const Text('Einstellungen speichern'),
            ),
          ],
        ),
      ),
    );
  }
}

class FilesPage extends StatefulWidget {
  const FilesPage({super.key});

  @override
  State<FilesPage> createState() => _FilesPageState();
}

class _FilesPageState extends State<FilesPage> {
  List<File> _images = <File>[];
  List<String> _webImages = <String>[];

  @override
  void initState() {
    super.initState();
    _loadImages();
  }

  Future<void> _loadImages() async {
    if (kIsWeb) {
      if (!mounted) return;
      setState(() {
        _webImages = AppImageStore.webImagePaths;
      });
      return;
    }

    final Directory directory = await _getStorageDirectory();
    final List<FileSystemEntity> files = directory.listSync();

    if (!mounted) return;
    setState(() {
      _images = files.whereType<File>().where((File file) {
        final String lower = file.path.toLowerCase();
        return lower.endsWith('.jpg') ||
            lower.endsWith('.jpeg') ||
            lower.endsWith('.png');
      }).toList();
    });
  }

  Future<Directory> _getStorageDirectory() async {
    if (kIsWeb) {
      throw UnsupportedError(
        'Speichern von Dateien ist im Web nicht unterstützt.',
      );
    } else {
      return await getApplicationDocumentsDirectory();
    }
  }

  @override
  Widget build(BuildContext context) {
    final bool noImages = kIsWeb ? _webImages.isEmpty : _images.isEmpty;
    final int imageCount = kIsWeb ? _webImages.length : _images.length;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Dateien'),
        actions: <Widget>[
          IconButton(icon: const Icon(Icons.refresh), onPressed: _loadImages),
        ],
      ),
      body: noImages
          ? const Center(child: Text('Keine Bilder vorhanden'))
          : GridView.builder(
              padding: const EdgeInsets.all(8),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                crossAxisSpacing: 8,
                mainAxisSpacing: 8,
              ),
              itemCount: imageCount,
              itemBuilder: (BuildContext context, int index) {
                if (kIsWeb) {
                  final String imageUrl = _webImages[index];
                  return GestureDetector(
                    onTap: () => _showWebImage(context, imageUrl),
                    child: Image.network(imageUrl, fit: BoxFit.cover),
                  );
                }

                final File image = _images[index];
                return GestureDetector(
                  onTap: () => _showImage(context, image),
                  child: Image.file(image, fit: BoxFit.cover),
                );
              },
            ),
    );
  }

  void _showWebImage(BuildContext context, String imageUrl) {
    showDialog<void>(
      context: context,
      builder: (BuildContext dialogContext) => Dialog(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Image.network(imageUrl),
            OverflowBar(
              children: <Widget>[
                TextButton(
                  onPressed: () => Navigator.pop(dialogContext),
                  child: const Text('SchlieBen'),
                ),
                ElevatedButton(
                  onPressed: () => _uploadWebImage(dialogContext, imageUrl),
                  child: const Text('Hochladen (Dummy)'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  void _showImage(BuildContext context, File image) {
    showDialog<void>(
      context: context,
      builder: (BuildContext dialogContext) => Dialog(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Image.file(image),
            OverflowBar(
              children: <Widget>[
                TextButton(
                  onPressed: () => Navigator.pop(dialogContext),
                  child: const Text('SchlieBen'),
                ),
                ElevatedButton(
                  onPressed: () => _uploadImage(dialogContext, image),
                  child: const Text('Hochladen (Dummy)'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Future<void> _uploadImage(BuildContext dialogContext, File image) async {
    try {
      // TODO: Spater durch echte API-URL und echten HTTP-Upload ersetzen.
      final Uri fakeUri = Uri.parse('https://example.invalid/upload');
      final http.MultipartRequest request =
          http.MultipartRequest('POST', fakeUri)
            ..fields['description'] = 'Foto von der App'
            ..files.add(await http.MultipartFile.fromPath('image', image.path));

      final String simulatedResponseBody = jsonEncode(<String, Object>{
        'success': true,
        'message': 'Dummy-Upload erfolgreich simuliert (kein echter Server)',
        'filename': path.basename(image.path),
        'fieldCount': request.fields.length,
      });

      final http.Response simulatedResponse = http.Response(
        simulatedResponseBody,
        200,
      );
      final Map<String, dynamic> jsonResponse =
          json.decode(simulatedResponse.body) as Map<String, dynamic>;

      if (!mounted || !dialogContext.mounted) return;
      Navigator.pop(dialogContext);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(jsonResponse['message'] as String),
          backgroundColor: Colors.green,
        ),
      );
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Fehler beim Hochladen: $e'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  Future<void> _uploadWebImage(
    BuildContext dialogContext,
    String imageUrl,
  ) async {
    try {
      // TODO: Spater durch echte API-URL und echten HTTP-Upload ersetzen.
      final Uri fakeUri = Uri.parse('https://example.invalid/upload');
      final http.Request request = http.Request('POST', fakeUri)
        ..body = jsonEncode(<String, String>{
          'description': 'Foto von der App',
          'imageUrl': imageUrl,
        });

      final String simulatedResponseBody = jsonEncode(<String, Object>{
        'success': true,
        'message': 'Dummy-Upload erfolgreich simuliert (kein echter Server)',
        'filename': path.basename(Uri.parse(imageUrl).path),
        'contentLength': request.body.length,
      });

      final http.Response simulatedResponse = http.Response(
        simulatedResponseBody,
        200,
      );
      final Map<String, dynamic> jsonResponse =
          json.decode(simulatedResponse.body) as Map<String, dynamic>;

      if (!mounted || !dialogContext.mounted) return;
      Navigator.pop(dialogContext);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(jsonResponse['message'] as String),
          backgroundColor: Colors.green,
        ),
      );
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Fehler beim Hochladen: $e'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }
}
