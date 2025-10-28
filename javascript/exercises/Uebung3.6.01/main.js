
// a) Definiere eine Variable alter mit dem Wert 30 und eine Variable name mit dem Wert "Max". Zeige beide Werte mit Hilfe von console.log() in der Konsole an.  

// b) Konvertiere das Alter von einem String in eine Zahl und addiere 5 Jahre. Zeige das Ergebnis in der Konsole an. 

// c) Überprüfe, ob eine Variable besucher undefined ist. Wenn ja, weise ihr den Wert "Neuer Besucher" zu und zeige diesen Wert in der Konsole an. 

// d) Erstelle eine Variable loginVersuche mit dem Wert null. Erhöhe den Wert um 1, wenn ein Login-Versuch unternommen wird. Zeige den Wert nach dem Versuch in der Konsole an. 

// e) Überprüfe, ob ein String leerString leer ist. Wenn ja, zeige "String ist leer" in der Konsole an. Wenn nicht, zeige den Wert des Strings an. 

// f) Konvertiere eine Variable zahlString mit dem Wert "1234.56" zuerst in eine ganze Zahl und dann in eine Gleitkommazahl. Zeige beide Ergebnisse in der Konsole an. 
    
    // a)
    let alter = 30, name = "Max";
    console.log(alter, name);
    //b)
    let alter2 = "40";
    // let neuAlter = alter + 5 Funktioniert hier nicht, da es sich um den plus operanden handelt und er 405 Ausgibt im log. Ddaher ist eine Umwandlung nötig. Ich wandle mit Unary um:
    let neuAlter=+alter2+5;
    console.log(neuAlter);
    //c)
    let var3;
    console.log("var3",var3); // log:undefined
    var3="Neuer Besucher";
    console.log("var3",var3);
        //Bessere Lösung: 
        //let besucher;
        // if (typeof besucher === "undefined"){
        //}besucher = "Neuer Besucher";
        // console.log(besucher);


    //d)
    let loginVersuche = null;
    loginAttempt = true;
    console.log("Login Versuche:", loginVersuche);
    // loginAttempt soll true sein, wenn true dann count +1, wenn false dann nix.
    if (loginAttempt = true){
        (loginVersuche = loginVersuche+1);
    }
     console.log("Login Versuche:", loginVersuche);       
    //e)
    let str1 = [];
    leerString = str1.toString();
    console.log(leerString, typeof leerString);
    if (leerString >0){
        console.log("Der Wert des Strings ist:", leerString);
        } else {
            console.log("Der String ist leer!");
        }
    // f)
    let zahlString = "1234.56"
    intVar = parseInt(zahlString);
    floatVar = parseFloat(zahlString);
    console.log(intVar, floatVar)