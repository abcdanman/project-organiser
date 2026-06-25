#!/usr/bin/env python3
"""Generate SVG logos for all FYP UM projects"""
from pathlib import Path
import shutil

HERE = Path(__file__).parent
BASE = HERE.parent
LOGOS = HERE / "logos"
LOGOS.mkdir(exist_ok=True)

def svg(g1, g2, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{g1}"/><stop offset="100%" stop-color="{g2}"/></linearGradient></defs><rect width="100" height="100" rx="22" fill="url(#g)"/>{body}</svg>'

PROJECTS = [
    ("project-organiser", "#7c3aed", "#4f46e5",
     # Folder with grid dots
     '<path fill="white" opacity="0.9" d="M18 44 Q18 36 26 36 H40 L46 30 H74 Q82 30 82 38 V72 Q82 80 74 80 H26 Q18 80 18 72 Z"/>'
     '<circle cx="38" cy="54" r="4.5" fill="#7c3aed"/><circle cx="50" cy="54" r="4.5" fill="#7c3aed"/><circle cx="62" cy="54" r="4.5" fill="#7c3aed"/>'
     '<circle cx="38" cy="66" r="4.5" fill="#7c3aed"/><circle cx="50" cy="66" r="4.5" fill="#7c3aed"/><circle cx="62" cy="66" r="4.5" fill="#7c3aed"/>',
     None),

    ("antigravity-yapping", "#7c3aed", "#9333ea",
     # Speech bubble with typing dots
     '<path fill="white" opacity="0.95" d="M20 30 Q20 20 30 20 H70 Q80 20 80 30 V56 Q80 66 70 66 H54 L44 78 L46 66 H30 Q20 66 20 56 Z"/>'
     '<circle cx="38" cy="43" r="5.5" fill="#7c3aed"/><circle cx="50" cy="43" r="5.5" fill="#7c3aed"/><circle cx="62" cy="43" r="5.5" fill="#7c3aed"/>',
     "Antigravity Yapping"),

    ("testing-yapping", "#0891b2", "#0369a1",
     # Document with lines
     '<path fill="white" opacity="0.9" d="M28 14 H60 L76 30 V86 Q76 92 70 92 H30 Q24 92 24 86 V20 Q24 14 28 14 Z"/>'
     '<path fill="#0891b2" d="M60 14 V30 H76"/>'
     '<rect x="34" y="42" width="28" height="5" rx="2.5" fill="#0891b2"/>'
     '<rect x="34" y="54" width="22" height="5" rx="2.5" fill="#0891b2"/>'
     '<rect x="34" y="66" width="26" height="5" rx="2.5" fill="#0891b2"/>',
     "Testing yapping"),

    ("jomcuti-app", "#f59e0b", "#ea580c",
     # Sun with rays
     '<circle cx="50" cy="50" r="17" fill="white" opacity="0.95"/>'
     '<rect x="47" y="14" width="6" height="13" rx="3" fill="white" opacity="0.9"/>'
     '<rect x="47" y="73" width="6" height="13" rx="3" fill="white" opacity="0.9"/>'
     '<rect x="14" y="47" width="13" height="6" rx="3" fill="white" opacity="0.9"/>'
     '<rect x="73" y="47" width="13" height="6" rx="3" fill="white" opacity="0.9"/>'
     '<rect x="22.5" y="18.5" width="6" height="13" rx="3" fill="white" opacity="0.9" transform="rotate(45 25.5 25)"/>'
     '<rect x="68.5" y="18.5" width="6" height="13" rx="3" fill="white" opacity="0.9" transform="rotate(-45 74.5 25)"/>'
     '<rect x="22.5" y="68.5" width="6" height="13" rx="3" fill="white" opacity="0.9" transform="rotate(-45 25.5 75)"/>'
     '<rect x="68.5" y="68.5" width="6" height="13" rx="3" fill="white" opacity="0.9" transform="rotate(45 74.5 75)"/>',
     "jomcuti-app"),

    ("um-waze", "#0284c7", "#1d4ed8",
     # Location pin (teardrop with inner dot)
     '<path fill="white" opacity="0.95" d="M50 14 C31 14 18 27 18 44 C18 62 50 86 50 86 C50 86 82 62 82 44 C82 27 69 14 50 14 Z"/>'
     '<circle cx="50" cy="42" r="11" fill="#0284c7"/>',
     "um-waze"),

    ("um-eagle-eye", "#8b5cf6", "#6d28d9",
     # Eye with iris
     '<path fill="white" opacity="0.9" d="M10 50 Q28 20 50 20 Q72 20 90 50 Q72 80 50 80 Q28 80 10 50 Z"/>'
     '<circle cx="50" cy="50" r="16" fill="#8b5cf6"/>'
     '<circle cx="50" cy="50" r="7" fill="white"/>',
     "UMEagleEye-FORKED-FOR-EBSI"),

    ("game", "#10b981", "#0d9488",
     # Game controller
     '<path fill="white" opacity="0.9" d="M18 42 Q18 32 28 32 H72 Q82 32 82 42 V60 Q82 72 70 72 H57 L50 67 L43 72 H30 Q18 72 18 60 Z"/>'
     '<rect x="35" y="46" width="5" height="14" rx="2.5" fill="#10b981"/>'
     '<rect x="29" y="50" width="14" height="5" rx="2.5" fill="#10b981"/>'
     '<circle cx="62" cy="47" r="4" fill="#10b981"/>'
     '<circle cx="70" cy="54" r="4" fill="#10b981"/>'
     '<circle cx="62" cy="61" r="4" fill="#10b981"/>'
     '<circle cx="54" cy="54" r="4" fill="#10b981"/>',
     "Game"),

    ("snap-challenge", "#ec4899", "#be185d",
     # Camera body + lens
     '<path fill="white" opacity="0.9" d="M14 40 H32 L40 30 H60 L68 40 H86 Q90 40 90 44 V72 Q90 76 86 76 H14 Q10 76 10 72 V44 Q10 40 14 40 Z"/>'
     '<circle cx="50" cy="57" r="15" fill="#ec4899"/>'
     '<circle cx="50" cy="57" r="9" fill="white"/>'
     '<circle cx="50" cy="57" r="5" fill="#ec4899"/>'
     '<circle cx="74" cy="44" r="4" fill="#ec4899"/>',
     "snapchallenge"),

    ("dr-trader", "#ef4444", "#b91c1c",
     # Bar chart rising + arrow
     '<rect x="16" y="58" width="14" height="20" rx="3" fill="white" opacity="0.6"/>'
     '<rect x="34" y="46" width="14" height="32" rx="3" fill="white" opacity="0.75"/>'
     '<rect x="52" y="32" width="14" height="46" rx="3" fill="white" opacity="0.9"/>'
     '<path stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M70 22 L82 22 L82 34"/>'
     '<path stroke="white" stroke-width="4" stroke-linecap="round" fill="none" d="M68 36 L82 22"/>',
     "Dr Trader"),

    ("game-optimizer", "#f59e0b", "#b45309",
     # Lightning bolt
     '<path fill="white" opacity="0.95" d="M58 14 L34 52 H51 L42 86 L66 48 H49 Z"/>',
     "Game Optimizer"),

    ("storage-cleaner", "#64748b", "#334155",
     # 4-point sparkle + center
     '<path fill="white" opacity="0.9" d="M50 14 L55 45 L86 50 L55 55 L50 86 L45 55 L14 50 L45 45 Z"/>'
     '<circle cx="50" cy="50" r="7" fill="white"/>',
     "Storage Cleaner"),

    ("gmail-bot", "#dc2626", "#9f1239",
     # Envelope with checkmark badge
     '<path fill="white" opacity="0.9" d="M12 30 H88 V72 Q88 78 82 78 H18 Q12 78 12 72 Z"/>'
     '<path fill="#dc2626" d="M12 30 L50 58 L88 30"/>'
     '<circle cx="72" cy="70" r="14" fill="#dc2626" stroke="white" stroke-width="2.5"/>'
     '<path stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M65 70 L70 75 L79 63"/>',
     "Gmail bot"),

    ("telegram-wakeup", "#0ea5e9", "#0369a1",
     # Bell shape
     '<path fill="white" opacity="0.9" d="M50 14 C50 14 76 18 78 46 L82 70 H18 L22 46 C24 18 50 14 50 14 Z"/>'
     '<rect x="40" y="70" width="20" height="8" rx="4" fill="white" opacity="0.9"/>'
     '<circle cx="50" cy="82" r="8" fill="white" opacity="0.9"/>'
     '<rect x="44" y="8" width="12" height="12" rx="6" fill="white" opacity="0.9"/>',
     "Telegram wake up"),

    ("otonoco-compliance", "#6366f1", "#4338ca",
     # Shield with checkmark
     '<path fill="white" opacity="0.9" d="M50 14 L78 24 V50 Q78 70 50 82 Q22 70 22 50 V24 Z"/>'
     '<path stroke="#6366f1" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none" d="M36 50 L46 62 L64 38"/>',
     "Otonoco Compliance"),
]

for name, g1, g2, body, copy_to in PROJECTS:
    content = svg(g1, g2, body)
    out = LOGOS / f"{name}.svg"
    out.write_text(content, encoding="utf-8")
    print(f"  {name}.svg")
    if copy_to:
        dest = BASE / copy_to / "logo.svg"
        dest.write_text(content, encoding="utf-8")

print(f"\nDone — {len(PROJECTS)} logos in {LOGOS}")
