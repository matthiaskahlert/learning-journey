const i18nJson = `
{
  "de": {
    "nav.about": "Über mich",
    "nav.skills": "Skills",
    "nav.services": "Services",
    "nav.projects": "Projekte",
    "nav.experience": "Erfahrung",
    "nav.contact": "Kontakt",
    "hero.eyebrow": "Portfolio",
    "hero.text": "Ich sorge dafür, dass Software stabil läuft – bevor es deine Nutzer merken. Mit über 10 Jahren Erfahrung in QA, Live-Systemen und Release Management.",
    "hero.cta": "Projekte ansehen",
    "about.title": "Über mich",
    "about.text": "Ich unterstütze Teams dabei, Qualität frühzeitig in Produkte zu integrieren – mit Fokus auf Exploratory Testing, API Testing und strukturierte Qualitätssicherung.",
    "skills.title": "Skills",
    "services.title": "Services",
    "services.s1.title": "QA Leadership",
    "services.s1.text": "Aufbau von QA-Prozessen, Teststrategie und Team-Guidance.",
    "services.s2.title": "Test Management",
    "services.s2.text": "Planung, Priorisierung und Absicherung von Releases.",
    "services.s3.title": "Quality Consulting",
    "services.s3.text": "Audit bestehender Prozesse und Einführung nachhaltiger Qualitätsmetriken.",
    "projects.title": "Projekte",
    "projects.p1.title": "Seafight (Live MMO)",
    "projects.p1.text": "Qualitätssicherung für ein Live-MMO mit Millionen von Spielern. Fokus auf Exploratory Testing, Regression und schnelle Analyse von Live-Issues.",
    "projects.p2.title": "DarkOrbit (Live Game)",
    "projects.p2.text": "Technische Validierung komplexer Features und Events in einer produktiven Live-Umgebung. Enge Zusammenarbeit mit Entwicklung zur Sicherstellung stabiler Releases.",
    "projects.p3.title": "Farmerama",
    "projects.p3.text": "Absicherung von Content-Updates und Events mit Fokus auf Stabilität, Performance und User Experience.",
    "projects.p4.title": "Supremacy / Iron Order / Call of War",
    "projects.p4.text": "QA Leadership für Live-Strategiespiele. Verbesserung der Release-Qualität durch strukturierte Testprozesse und enge Zusammenarbeit mit Entwicklungsteams.",
    "experience.title": "Erfahrung",
    "exp.1.title": "QA Lead – Bytro Labs",
    "exp.1.meta": "2024 – 2025",
    "exp.1.text": "Verantwortung für Release-Qualität mehrerer Live-Strategiespiele. Einführung strukturierter QA-Prozesse und enge Zusammenarbeit mit Entwicklungsteams zur nachhaltigen Verbesserung der Stabilität.",
    "exp.1.stack": "QA Leadership · Test Strategy · Live Ops · Release Management",
    "exp.2.title": "IT Test Manager – Andreas Paulsen GmbH",
    "exp.2.meta": "2023",
    "exp.2.text": "Planung und Steuerung von Testaktivitäten für geschäftskritische Systeme. Fokus auf End-to-End Validierung und stabile Releases in komplexen Systemlandschaften.",
    "exp.2.stack": "Test Management · E2E Testing · Jira · Confluence · Stakeholder Communication",
    "exp.3.title": "QA Director – Bigpoint",
    "exp.3.meta": "2021 – 2023",
    "exp.3.text": "Aufbau und Steuerung von QA-Strategien für mehrere Live-Games. Definition von Qualitätsmetriken und enge Abstimmung mit Produktion und Plattform-Teams.",
    "exp.3.stack": "QA Strategy · KPIs · Cross-Team Leadership · Live Games",
    "exp.4.title": "Lead QA Tester – Bigpoint",
    "exp.4.meta": "2015 – 2021",
    "exp.4.text": "Hands-on Testing für Live-Features mit Fokus auf Exploratory Testing, Performance und technische Validierung von Backend- und API-Systemen.",
    "exp.4.stack": "Exploratory Testing · SQL · API Testing · Git",
    "contact.title": "Kontakt",
    "contact.text": "Lass uns über Qualität, Testing und stabile Releases sprechen.",
    "contact.cta": "Kontakt aufnehmen"
  },
  "en": {
    "nav.about": "About",
    "nav.skills": "Skills",
    "nav.services": "Services",
    "nav.projects": "Projects",
    "nav.experience": "Experience",
    "nav.contact": "Contact",
    "hero.eyebrow": "Portfolio",
    "hero.text": "I make sure your software works — before your users notice issues. With 10+ years of experience in QA, live systems and release management.",
    "hero.cta": "View projects",
    "about.title": "About",
    "about.text": "I help teams build quality into products early, with a focus on exploratory testing, API testing and sustainable quality assurance.",
    "skills.title": "Skills",
    "services.title": "Services",
    "services.s1.title": "QA Leadership",
    "services.s1.text": "Building QA processes, test strategy and team guidance.",
    "services.s2.title": "Test Management",
    "services.s2.text": "Planning, prioritization and release quality coverage.",
    "services.s3.title": "Quality Consulting",
    "services.s3.text": "Auditing existing workflows and introducing practical quality metrics.",
    "projects.title": "Projects",
    "projects.p1.title": "Seafight (Live MMO)",
    "projects.p1.text": "Quality assurance for a live MMO with millions of players. Focus on exploratory testing, regression and fast live issue analysis.",
    "projects.p2.title": "DarkOrbit (Live Game)",
    "projects.p2.text": "Technical validation of complex features and events in a live production environment. Close collaboration with developers to ensure stable releases.",
    "projects.p3.title": "Farmerama",
    "projects.p3.text": "Ensured quality of content updates and live events with focus on stability, performance and user experience.",
    "projects.p4.title": "Supremacy / Iron Order / Call of War",
    "projects.p4.text": "QA leadership for live strategy games. Improved release quality through structured testing processes and strong dev collaboration.",
    "experience.title": "Experience",
    "exp.1.title": "QA Lead – Bytro Labs",
    "exp.1.meta": "2024 – 2025",
    "exp.1.text": "Responsible for release quality of multiple live strategy games. Introduced structured QA processes and closely collaborated with development teams to sustainably improve stability.",
    "exp.1.stack": "QA Leadership · Test Strategy · Live Ops · Release Management",
    "exp.2.title": "IT Test Manager – Andreas Paulsen GmbH",
    "exp.2.meta": "2023",
    "exp.2.text": "Planned and managed test activities for business-critical systems. Focused on end-to-end validation and stable releases in complex system landscapes.",
    "exp.2.stack": "Test Management · E2E Testing · Jira · Confluence · Stakeholder Communication",
    "exp.3.title": "QA Director – Bigpoint",
    "exp.3.meta": "2021 – 2023",
    "exp.3.text": "Established and managed QA strategies for multiple live games. Defined quality metrics and closely coordinated with production and platform teams.",
    "exp.3.stack": "QA Strategy · KPIs · Cross-Team Leadership · Live Games",
    "exp.4.title": "Lead QA Tester – Bigpoint",
    "exp.4.meta": "2015 – 2021",
    "exp.4.text": "Hands-on testing for live features with a focus on exploratory testing, performance, and technical validation of backend and API systems.",
    "exp.4.stack": "Exploratory Testing · SQL · API Testing · Git",
    "contact.title": "Contact",
    "contact.text": "Let's talk about quality, testing and stable releases.",
    "contact.cta": "Get in touch"
  }
}
`;

const translations = JSON.parse(i18nJson);
const DEFAULT_LANG = 'de';
const SUPPORTED_LANGS = ['de', 'en'];

let nameEl;
let roleEl;
let themeToggle;
let langToggle;
let navToggle;
let navMenu;

const rolesByLang = {
  de: [
    'Senior QA Engineer',
    'QA Lead für Live-Systeme',
    'Testmanager für stabile Releases'
  ],
  en: [
    'Senior QA Engineer',
    'QA Lead for Live Systems',
    'Test Manager for Reliable Releases'
  ]
};

let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;
const storedLang = localStorage.getItem('lang');
let currentLang = SUPPORTED_LANGS.includes(storedLang) ? storedLang : DEFAULT_LANG;
let currentRoles = rolesByLang[currentLang];
let typewriterTimeoutId;

function typeRole() {
  const role = currentRoles[roleIndex];
  if (isDeleting) {
    charIndex -= 1;
  } else {
    charIndex += 1;
  }
  const next = role.slice(0, charIndex);
  roleEl.textContent = next;

  if (!isDeleting && charIndex === role.length) {
    isDeleting = true;
    typewriterTimeoutId = setTimeout(typeRole, 1200);
    return;
  }

  if (isDeleting && charIndex === 0) {
    isDeleting = false;
    roleIndex = (roleIndex + 1) % currentRoles.length;
  }

  typewriterTimeoutId = setTimeout(typeRole, isDeleting ? 55 : 95);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
}

function t(key) {
  return translations[currentLang]?.[key] || key;
}

function applyLanguage() {
  currentRoles = rolesByLang[currentLang] || rolesByLang[DEFAULT_LANG];
  document.documentElement.lang = currentLang;
  document.querySelectorAll('[data-i18n]').forEach((node) => {
    node.textContent = t(node.dataset.i18n);
  });
  localStorage.setItem('lang', currentLang);
  langToggle.textContent = currentLang === 'de' ? 'EN' : 'DE';
  langToggle.setAttribute(
    'aria-label',
    currentLang === 'de' ? 'Zu Englisch wechseln' : 'Switch to German'
  );
}

function resetTypewriter() {
  clearTimeout(typewriterTimeoutId);
  roleIndex = 0;
  charIndex = 0;
  isDeleting = false;
  if (roleEl) {
    roleEl.textContent = '';
  }
}

function startTypewriter() {
  resetTypewriter();
  typeRole();
}

function setupReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  document.querySelectorAll('.reveal').forEach((section) => observer.observe(section));
}

function setupMouseReactiveBg() {
  window.addEventListener('mousemove', (event) => {
    const x = (event.clientX / window.innerWidth) * 100;
    const y = (event.clientY / window.innerHeight) * 100;
    document.documentElement.style.setProperty('--mouse-x', `${x}%`);
    document.documentElement.style.setProperty('--mouse-y', `${y}%`);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  nameEl = document.getElementById('heroName');
  roleEl = document.getElementById('roleTypewriter');
  themeToggle = document.getElementById('themeToggle');
  langToggle = document.getElementById('langToggle');
  navToggle = document.querySelector('.nav-toggle');
  navMenu = document.getElementById('nav-menu');

  navToggle?.addEventListener('click', () => {
    const open = navMenu.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });

  themeToggle?.addEventListener('click', () => {
    const nextTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
  });

  langToggle?.addEventListener('click', () => {
    currentLang = currentLang === 'de' ? 'en' : 'de';
    applyLanguage();
    startTypewriter();
  });

  const preferredTheme = localStorage.getItem('theme') || 'light';
  applyTheme(preferredTheme);
  applyLanguage();
  setupReveal();
  setupMouseReactiveBg();
  setTimeout(() => nameEl?.classList.add('ready'), 120);
  startTypewriter();
});