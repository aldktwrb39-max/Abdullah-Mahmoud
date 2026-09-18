# Generate a single self-contained HTML file for Tadabbur Quran App
html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>تطبيق تدبّر - تدبر آيات القرآن الكريم</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #1B4332;
      --primary-light: #2D6A4F;
      --accent: #C28B47;
      --accent-soft: #F4EAD8;
      --bg: #F8F5EE;
      --card-bg: #FFFFFF;
      --text-main: #232D28;
      --text-muted: #586560;
      --border: #E8E2D5;
      --radius: 20px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Tajawal', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      display: flex;
      justify-content: center;
      min-height: 100vh;
      padding: 16px;
    }

    .app-container {
      width: 100%;
      max-width: 480px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    header {
      text-align: center;
      padding: 12px 0 6px 0;
    }

    header h1 {
      font-family: 'Amiri', serif;
      font-size: 32px;
      color: var(--primary);
      margin-bottom: 4px;
    }

    header p {
      font-size: 14px;
      color: var(--text-muted);
    }

    .tags-container {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }
    .tags-container::-webkit-scrollbar { display: none; }

    .tag-btn {
      background: white;
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      font-family: 'Tajawal', sans-serif;
    }

    .tag-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .card {
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 24px;
      border: 1px solid var(--border);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
      display: flex;
      flex-direction: column;
      gap: 18px;
      position: relative;
    }

    .card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .surah-badge {
      background: var(--accent-soft);
      color: var(--accent);
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
    }

    .action-icons {
      display: flex;
      gap: 10px;
    }

    .icon-btn {
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px;
      color: var(--text-muted);
      transition: 0.2s;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .icon-btn:hover {
      background: #F0ECE1;
      color: var(--primary);
    }

    .icon-btn.bookmarked {
      color: var(--accent);
    }

    .ayah-text {
      font-family: 'Amiri', serif;
      font-size: 24px;
      line-height: 2.2;
      text-align: center;
      color: var(--primary);
      padding: 10px 0;
    }

    .divider {
      height: 1px;
      background: var(--border);
      width: 100%;
    }

    .section-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 15px;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 6px;
    }

    .section-content {
      font-size: 14.5px;
      line-height: 1.8;
      color: var(--text-muted);
    }

    .action-box {
      background: #F4F9F6;
      border-right: 4px solid var(--primary-light);
      padding: 12px 16px;
      border-radius: 8px;
    }

    .action-box .section-title {
      color: var(--primary-light);
    }

    .action-box .section-content {
      color: #264638;
      font-weight: 500;
    }

    .controls {
      display: flex;
      gap: 12px;
      margin-top: 8px;
    }

    .next-btn {
      flex: 1;
      background: var(--primary);
      color: white;
      border: none;
      border-radius: 14px;
      padding: 14px 20px;
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: background 0.2s;
      font-family: 'Tajawal', sans-serif;
    }

    .next-btn:hover {
      background: var(--primary-light);
    }

    .share-btn {
      background: white;
      border: 1px solid var(--border);
      color: var(--primary);
      border-radius: 14px;
      width: 50px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      transition: background 0.2s;
    }

    .share-btn:hover {
      background: #F0ECE1;
    }

    .toast {
      position: fixed;
      bottom: 24px;
      background: #232D28;
      color: white;
      padding: 10px 20px;
      border-radius: 30px;
      font-size: 13px;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      pointer-events: none;
    }

    .toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>

  <div class="app-container">
    <header>
      <h1>تَدَبُّر</h1>
      <p>آيات مُحكمات مع وقفات تدبر وتطبيق يومي</p>
    </header>

    <div class="tags-container" id="categoryContainer">
      <button class="tag-btn active" onclick="filterCategory('الكل', this)">الكل</button>
      <button class="tag-btn" onclick="filterCategory('طمأنينة', this)">طمأنينة</button>
      <button class="tag-btn" onclick="filterCategory('توبة', this)">توبة ورجاء</button>
      <button class="tag-btn" onclick="filterCategory('شكر', this)">شكر ونعمة</button>
      <button class="tag-btn" onclick="filterCategory('صبر', this)">صبر وفرج</button>
      <button class="tag-btn" onclick="showSaved(this)">المحفوظات ⭐</button>
    </div>

    <div class="card" id="verseCard">
      <div class="card-meta">
        <span class="surah-badge" id="surahBadge">سورة البقرة : آية 152</span>
        <div class="action-icons">
          <button class="icon-btn" id="favBtn" onclick="toggleFavorite()" title="حفظ في المفضلة">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
          </button>
        </div>
      </div>

      <div class="ayah-text" id="ayahText">
        ﴿ فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ ﴾
      </div>

      <div class="divider"></div>

      <div>
        <div class="section-title">
          <span>💡</span> وقفة تدبرية
        </div>
        <p class="section-content" id="tadabburText">
          لو لم يكن للعبد من جزاء الذكر إلا أن يذكره ملك الملوك وخالق الكون في ملأ عنده، لكفى به شرفاً وسكينة تملأ قلبه في زحام الدنيا وتقلباتها.
        </p>
      </div>

      <div class="action-box">
        <div class="section-title">
          <span>🌱</span> العمل بالآية
        </div>
        <p class="section-content" id="actionText">
          اجعل لسانك رطباً بالتسبيح والاستغفار في أوقات الانتظار والفراغ طوال هذا اليوم.
        </p>
      </div>
    </div>

    <div class="controls">
      <button class="share-btn" onclick="shareAyah()" title="مشاركة الآية">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
      </button>
      <button class="next-btn" onclick="nextAyah()">
        <span>آية تدبر أخرى</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
      </button>
    </div>
  </div>

  <div class="toast" id="toast">تم النسخ بنجاح</div>

  <script>
    const data = [
      {
        id: 1,
        surah: "البقرة",
        ayahNum: 152,
        category: "شكر",
        ayah: "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ",
        tadabbur: "لو لم يكن للعبد من جزاء الذكر إلا أن يذكره ملك الملوك وخالق الكون في ملأ عنده، لكفى به شرفاً وسكينة تملأ قلبه في زحام الدنيا وتقلباتها.",
        action: "اجعل لسانك رطباً بالتسبيح والاستغفار في أوقات الانتظار والفراغ طوال هذا اليوم."
      },
      {
        id: 2,
        surah: "الرعد",
        ayahNum: 28,
        category: "طمأنينة",
        ayah: "الَّذِينَ آمَنُوا وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ اللَّهِ ۗ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ",
        tadabbur: "القلب مجبول على القلق ولا يهدأ بقريب ولا بعيد، ولا بمال ولا جاه، إلا إذا سكن واتصل بركنه الشديد ومصدر الأمان المطلق سبحانه.",
        action: "كلما شعرت بتشتت أو ضيق اليوم، أوقف كل مشاغلك لدقيقة وردد: لا حول ولا قوة إلا بالله بحضور قلب."
      },
      {
        id: 3,
        surah: "الضحى",
        ayahNum: 3,
        category: "طمأنينة",
        ayah: "مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ",
        tadabbur: "انقطاع الوحي مؤقتاً لم يكن هجراناً بل إعداداً لخير أعظم. تأخر مطلوبك في الحياة ليس إهمالاً من الله، بل تدبير حكيم لم يحن وقته بعد.",
        action: "أحسن الظن بربك عند تأخر استجابة دعائك، وتذكر كم صرف عنك من شر كنت تحسبه خيراً."
      },
      {
        id: 4,
        surah: "الزمر",
        ayahNum: 53,
        category: "توبة",
        ayah: "قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا عَلَىٰ أَنفُسِهِمْ لَا تَقْنَطُوا مِن رَّحْمَةِ اللَّهِ ۚ إِنَّ اللَّهَ يَغْفِرُ الذُّنُوبَ جَمِيعًا",
        tadabbur: "لم يقل 'يا أيها العصاة'، بل نسبهم إليه متحبباً: 'يا عبادي'. رحمته سبحانه تتسع لكل ما اقترفته إن جئته منكسراً تائباً.",
        action: "استغفر الآن من ذنب يثقل قلبك واعزم على تركه في هذه اللحظة بصدق."
      },
      {
        id: 5,
        surah: "الإنشراح",
        ayahNum: 6,
        category: "صبر",
        ayah: "إِنَّ مَعَ الْعُسْرِ يُسْرًا",
        tadabbur: "جاء اليسر مقروناً بالعسر بلفظ 'مَعَ' وليس 'بَعْدَ'، ليدلك على أن فرج الله يتخلق في باطن الشدة ذاتها ولا ينفك عنها.",
        action: "انظر إلى الأمر المتعسر في حياتك اليوم، وابحث عن ثلاثة ألطاف خفية تحيط بك فيه."
      }
    ];

    let currentList = [...data];
    let currentIndex = 0;
    let savedIds = JSON.parse(localStorage.getItem('tadabbur_favs') || '[]');

    function renderAyah() {
      if (currentList.length === 0) {
        document.getElementById('surahBadge').innerText = "-";
        document.getElementById('ayahText').innerText = "لا توجد آيات محفوظة حالياً";
        document.getElementById('tadabburText').innerText = "اضغط على علامة الحفظ في أي آية لتظهر لك هنا.";
        document.getElementById('actionText').innerText = "تصفح بقية الأقسام لحفظ الآيات.";
        updateFavIcon(false);
        return;
      }

      const item = currentList[currentIndex];
      document.getElementById('surahBadge').innerText = `سورة ${item.surah} : آية ${item.ayahNum}`;
      document.getElementById('ayahText').innerText = `﴿ ${item.ayah} ﴾`;
      document.getElementById('tadabburText').innerText = item.tadabbur;
      document.getElementById('actionText').innerText = item.action;

      const isFav = savedIds.includes(item.id);
      updateFavIcon(isFav);
    }

    function nextAyah() {
      if (currentList.length <= 1) return;
      currentIndex = (currentIndex + 1) % currentList.length;
      renderAyah();
    }

    function updateFavIcon(isFav) {
      const btn = document.getElementById('favBtn');
      const svg = btn.querySelector('svg');
      if (isFav) {
        btn.classList.add('bookmarked');
        svg.setAttribute('fill', 'var(--accent)');
      } else {
        btn.classList.remove('bookmarked');
        svg.setAttribute('fill', 'none');
      }
    }

    function toggleFavorite() {
      if (currentList.length === 0) return;
      const item = currentList[currentIndex];
      const idx = savedIds.indexOf(item.id);
      if (idx > -1) {
        savedIds.splice(idx, 1);
        showToast("تم الحذف من المفضلة");
      } else {
        savedIds.push(item.id);
        showToast("تمت الإضافة إلى المفضلة ⭐");
      }
      localStorage.setItem('tadabbur_favs', JSON.stringify(savedIds));
      updateFavIcon(savedIds.includes(item.id));
    }

    function filterCategory(cat, el) {
      document.querySelectorAll('.tag-btn').forEach(btn => btn.classList.remove('active'));
      el.classList.add('active');

      if (cat === 'الكل') {
        currentList = [...data];
      } else {
        currentList = data.filter(d => d.category === cat);
      }
      currentIndex = 0;
      renderAyah();
    }

    function showSaved(el) {
      document.querySelectorAll('.tag-btn').forEach(btn => btn.classList.remove('active'));
      el.classList.add('active');
      currentList = data.filter(d => savedIds.includes(d.id));
      currentIndex = 0;
      renderAyah();
    }

    function shareAyah() {
      if (currentList.length === 0) return;
      const item = currentList[currentIndex];
      const text = `﴿ ${item.ayah} ﴾ [سورة ${item.surah}: ${item.ayahNum}]\n\n💡 وقفة تدبرية:\n${item.tadabbur}\n\n🌱 العمل بالآية:\n${item.action}\n\n- تطبيق تَدَبُّر`;
      
      if (navigator.share) {
        navigator.share({
          title: 'تدبر آية',
          text: text
        }).catch(() => {});
      } else {
        navigator.clipboard.writeText(text).then(() => {
          showToast("تم نسخ الآية والتدبر للمشاركة 📋");
        });
      }
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2200);
    }

    // تشغيل أولي
    renderAyah();
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File index.html generated successfully.")