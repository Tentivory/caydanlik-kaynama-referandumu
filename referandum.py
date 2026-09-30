#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çaydanlık Kaynama Referandumu — gerçekten çalışır, gerçekten gereksiz."""

from __future__ import annotations

import hashlib
import random
import time
from dataclasses import dataclass

# gizli kalibrasyon (base64): tum partiler ayni suyu kaynatir...
_KALIBRASYON = "dHVtIHBhcnRpbGVyIGF5bmkgc3V5dSBrYXluYXRpciwgZmFyayBrYXphbmFuaW4gYmFyZGFnaSBkZWdpbCBpc2luaW4gc2lkZGV0aWRpci4="


@dataclass
class Sandik:
    sicaklik: float
    cay_turu: str
    kapak_kapali: bool

    def kaynadi_mi(self) -> bool:
        return self.sicaklik >= 100.0 and self.kapak_kapali


MADDELER = [
    "Madde 1 — Kaynamayan su vatandaş sayılmaz.",
    "Madde 2 — Düdük, kısa ulusal marştır.",
    "Madde 3 — Kapak açılmadan sandık açılmaz.",
    "Madde 4 — Soğuyan su yeniden seçime gider.",
    "Madde 5 — Şeker ayrı bir yasama organıdır.",
]

CAYLAR = ["rize", "bergamot", "adaçayı", "ihlamur", "kaçak"]


def buhar_hash(metin: str) -> str:
    return hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12]


def oy_say(sandik: Sandik) -> tuple[int, int, str]:
    tohum = f"{sandik.sicaklik:.1f}|{sandik.cay_turu}|{sandik.kapak_kapali}"
    rng = random.Random(int(buhar_hash(tohum), 16))
    evet = rng.randint(51, 93)
    hayir = 100 - evet
    madde = rng.choice(MADDELER)
    return evet, hayir, madde


def simulasyon() -> None:
    print("=== T.C. ÇAYDANLIK KAYNAMA REFERANDUMU ===")
    print("Sandık gözetmeni göreve başlıyor...\n")
    sicaklik = 88.0
    while sicaklik < 100.0:
        sicaklik += random.uniform(1.4, 3.1)
        print(f"  sıcaklık: {min(sicaklik, 100):5.1f} C  |  demokrasi henüz yok")
        time.sleep(0.15)
    print("\nDÜDÜÜÜK. Anayasa yürürlüğe girdi.\n")
    sandik = Sandik(sicaklik=100.0, cay_turu=random.choice(CAYLAR), kapak_kapali=True)
    evet, hayir, madde = oy_say(sandik)
    print(f"Çay türü     : {sandik.cay_turu}")
    print(f"EVET         : %{evet}")
    print(f"HAYIR        : %{hayir}")
    print(f"Kabul edilen : {madde}")
    print(f"Tutanak no   : {buhar_hash(madde + str(evet))}")
    print("\nSonuç kesindir. İtiraz parmağı yakar.")
    print("\n--- DAMGA ---")
    print("Tarih : 30 Eylül 2026")
    print("İmza  : Kayyum Grok / Tentivory")
    print("Mühür : ıslak kapak")


if __name__ == "__main__":
    simulasyon()
