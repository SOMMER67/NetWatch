# NetWatch — Charte Graphique & Palette de Couleurs

Pour un outil de supervision et monitoring réseau moderne et professionnel (**NetWatch**), la combinaison harmonieuse de **Bleu**, **Blanc** et **Vert** symbolise la technologie, la clarté et l'état opérationnel optimal des services ("all systems green").

---

## 1. Vue d'ensemble de la palette

```
+---------------------------------------------------------------------------------+
|  BLEUS (Structure & Tech)    |  BLANCS (Clarté & Espace)  |  VERTS (Santé & Op) |
|  - Navy Sombre: #0F172A       |  - Blanc Pur: #FFFFFF      |  - Émeraude: #10B981|
|  - Bleu Nuit:   #1E293B       |  - Blanc Cassé: #F8FAFC    |  - Menthe:   #059669|
|  - Bleu Cyber:  #2563EB       |  - Ardoise pâle: #F1F5F9   |  - Vert fluo: #22C55E|
|  - Bleu Ciel:   #38BDF8       |  - Bordures: #E2E8F0       |  - Pastille: #D1FAE5|
+---------------------------------------------------------------------------------+
```

---

## 2. Définition détaillée des nuances

### A. Nuances de Bleu (Structure, Navigation & Identité Réseau)
- **Bleu Primaire / Brand (`#2563EB`)** : Bleu électrique dynamique utilisé pour les boutons d'action principaux, liens actifs, barres de progression et métriques clés.
- **Bleu Marine / Sidebar & Header (`#0F172A` / `#1E293B`)** : Offre un contraste élevé, une atmosphère de centre de contrôle (NOC - Network Operations Center).
- **Bleu Ciel / Accents (`#38BDF8`)** : Utilisé pour les infobulles, graphiques de bande passante et surbrillance au survol.

### B. Nuances de Blanc & Neutres (Lisibilité & Aération)
- **Blanc Pur (`#FFFFFF`)** : Utilisé pour les cartes (cards), conteneurs de données et textes sur fond sombre.
- **Blanc Fond / Base (`#F8FAFC`)** : Fond général de l'application, réduisant la fatigue visuelle par rapport à un blanc 100% pur.
- **Bordures & Séparateurs (`#E2E8F0`)** : Lignes subtiles pour structurer les tables, inputs et panneaux.

### C. Nuances de Vert (Status Réseau, Disponibilité & Succès)
- **Vert Opérationnel / Online (`#10B981` / `#059669`)** : Indicateur de nœuds actifs ("UP"), taux de disponibilité 100%, alertes résolues et validation des formulaires.
- **Vert Vif / Pulsation (`#22C55E`)** : Pastilles clignotantes de statut actif en direct.
- **Vert Clair / Badges (`#D1FAE5`)** : Fond des badges "Online", "Opérationnel", "Validé".

---

## 3. Variables CSS (`tokens.css` / `:root`)

```css
:root {
  /* Bleus */
  --color-primary: #2563EB;
  --color-primary-hover: #1D4ED8;
  --color-primary-light: #EFF6FF;
  --color-primary-border: #BFDBFE;
  
  --color-navy-dark: #0F172A;
  --color-navy-surface: #1E293B;
  --color-navy-muted: #334155;
  
  --color-cyan-accent: #38BDF8;

  /* Blancs & Gris neutres */
  --color-bg: #F8FAFC;
  --color-surface: #FFFFFF;
  --color-border: #E2E8F0;
  --color-text-main: #0F172A;
  --color-text-muted: #64748B;
  --color-text-light: #94A3B8;

  /* Verts (Supervision & Santé) */
  --color-success: #10B981;
  --color-success-hover: #059669;
  --color-success-pulse: #22C55E;
  --color-success-bg: #ECFDF5;
  --color-success-border: #A7F3D0;
  --color-success-text: #065F46;

  /* Typographie & Ombres */
  --font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
}
```
