# Kurd Chat & Domino Game — Official Project Source Code Archive ☀️📦
**پڕۆژەی فەرمیی کورد چات و یاریا دۆمینێ بە کۆدەکانی سەرچاوە بۆ ئەندرۆید و وێب**

---

## 📥 Direct Downloads for Android Phone (Google Chrome)

| شێوازی داگرتن (Download Method) | بەستەر (Link) | تێبینی (Note) |
| :--- | :--- | :--- |
| **داگرتنی ڕاستەوخۆ بە یەک کلیک (One-Click ZIP)** | [`kurd-chat-project.zip`](./kurd-chat-project.zip) | فایلی ڕاستەقینەی ZIP ئامادەکراو بۆ داگرتن |
| **پەڕەی داگرتنی خێرا (Offline Downloader)** | [`kurd_chat_project_download.html`](./kurd_chat_project_download.html) | بەبێ کێشەی Security Cookie لە ئەندرۆید کاردەکات |
| **سێرڤەری ڕاستەوخۆ (App Server ZIP)** | [داگرتن لە سێرڤەر](/kurd-chat-project.zip) | ڕاستەوخۆ لە ڕێگەی سێرڤەری سەرەکی پڕۆژە |
| **پەڕەی داگرتنی گشتی (Web Downloader)** | [پەڕەی فەرمی داگرتن](/download) | داگرتنی ئۆتۆماتیکی لە کرۆمدا دەست پێدەکات |

---

## 📱 چۆنێتی داگرتن لەسەر مۆبایلی ئەندرۆید (Google Chrome)

1. **ڕێگەی یەکەم (خێراترین و دڵنیاترین):**
   - کلیک لە فایلی هاوپێچکراوی **`kurd-chat-project.zip`** بکە لە تەنیشت یان سەرووی ئەم نامەیە.
   - داگرتن دەستپێدەکات و ڕاستەوخۆ دەچێتە بوخچەی `Downloads` لە مۆبایلەکەتدا.

2. **ڕێگەی دووەم (لە وێبگەڕی کرۆمدا):**
   - بچۆ پەڕەی [`/download`](/download) یان [`/download-offline.html`](/download-offline.html).
   - دوگمەی سەوزی **📥 داگرتنی ڕاستەوخۆی ZIP** دابگرە.
   - فایلی تەواوی پڕۆژەکە بە قەبارەی نزیکەی **٢ مێگابایت** لەسەر مۆبایلەکەت دادەبەزێت بەبێ پێویستی بە ئەنتەرنێتی تر.

---

## 🗂️ ناوەرۆکی فایلی ZIP (Project Contents)

ئەم فایلە ٦٧ فایلی سەرەکی پڕۆژەکەی لەخۆ گرتووە:
- **`server.ts`**: سێرڤەری تەواوی Node.js Express بە سیستەمی نامەی خێرا (SSE)، پەژراندنی هەژمار (Pejirandina Hesabê)، پارەدان و دەستپێکەری ئەدمین.
- **`src/`**: هەموو پێکهاتەکانی React 19، Tailwind CSS v4، و یاریا دۆمینێ:
  - `src/components/DominoLiveView.tsx` — ژووری ڕاستەوخۆی یاریا دۆمینێ بە دەنگی کوردی و هاوڕێیان
  - `src/components/AccountVerificationModal.tsx` — مۆداڵی فەرمیی پەژراندنی هەژمار (Blue Badge)
  - `src/components/AdminPanelModal.tsx` — پانێڵی کۆنتڕۆڵی بەڕێوەبەری گشتی سەباح سندى
  - `src/components/StoriesFeedView.tsx` & `StoryViewer.tsx` — ستۆریی کوردی بە وێنە و ڕەنگەکان
  - `src/components/VoiceChatModal.tsx` — تۆمارکردن و ناردنی دەنگی ڕاستەقینە
  - `src/components/CoinWalletModal.tsx` — جزدانی کۆینەکان و دیارییە کوردییەکان
- **`public/`**: هەموو وێنە و ئایکۆنەکانی PWA و نەخشەی کوردستان.
- **`package.json`** & **`vite.config.ts`**: ڕێکخستنەکانی کەرەستە و پڕۆژە.

---
*تێبینی: سەرجەم کۆدەکان بە شێوازی فەرمی و بە زمانی کوردی (سۆرانی و بادینی) بە تایبەتمەندی RTL پەرەیان پێدراوە.*
