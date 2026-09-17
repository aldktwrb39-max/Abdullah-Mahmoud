import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:share_plus/share_plus.dart';

import 'models/tadabbur_model.dart';
import 'services/quran_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // تهيئة قاعدة البيانات المحلية Hive
  await Hive.initFlutter();
  await Hive.openBox('favorites_box');

  runApp(const TadabburApp());
}

class TadabburApp extends StatelessWidget {
  const TadabburApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'تدبّر',
      debugShowCheckedModeBanner: false,
      locale: const Locale('ar', 'SA'),
      supportedLocales: const [Locale('ar', 'SA')],
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color(0xFFF9F6F0), // خلفية ورق طبيعية هادئة
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF1B4332), // لون أخضر غامق إسلامي وراقي
          primary: const Color(0xFF1B4332),
          secondary: const Color(0xFFD4A373),
        ),
        textTheme: GoogleFonts.tajawalTextTheme(),
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late List<TadabburItem> items;
  int currentIndex = 0;
  final Box favoritesBox = Hive.box('favorites_box');

  @override
  void initState() {
    super.initState();
    items = QuranService.getSampleItems();
    // تحميل حالة المفضلة من التخزين المحلي
    for (var item in items) {
      item.isBookmarked = favoritesBox.containsKey(item.id);
    }
  }

  void _toggleBookmark(TadabburItem item) {
    setState(() {
      item.isBookmarked = !item.isBookmarked;
      if (item.isBookmarked) {
        favoritesBox.put(item.id, item.toMap());
      } else {
        favoritesBox.delete(item.id);
      }
    });
  }

  void _nextItem() {
    setState(() {
      currentIndex = (currentIndex + 1) % items.length;
    });
  }

  @override
  Widget build(BuildContext context) {
    final currentItem = items[currentIndex];

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        centerTitle: true,
        title: Text(
          'تدبُّر آية',
          style: GoogleFonts.amiri(
            fontSize: 26,
            fontWeight: FontWeight.bold,
            color: const Color(0xFF1B4332),
          ),
        ),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
          child: Column(
            children: [
              // بطاقة الآية والتدبر
              Expanded(
                child: SingleChildScrollView(
                  child: Container(
                    padding: const EdgeInsets.all(24),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(24),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 16,
                          offset: const Offset(0, 6),
                        )
                      ],
                      border: Border.all(color: const Color(0xFFE8E2D5), width: 1.5),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        // اسم السورة ورقم الآية
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                              decoration: BoxDecoration(
                                color: const Color(0xFF1B4332).withOpacity(0.08),
                                borderRadius: BorderRadius.circular(12),
                              ),
                              child: Text(
                                'سورة ${currentItem.surahName} : آية ${currentItem.ayahNumber}',
                                style: const TextStyle(
                                  color: Color(0xFF1B4332),
                                  fontWeight: FontWeight.bold,
                                  fontSize: 13,
                                ),
                              ),
                            ),
                            IconButton(
                              icon: Icon(
                                currentItem.isBookmarked ? Icons.bookmark : Icons.bookmark_border,
                                color: currentItem.isBookmarked ? const Color(0xFFD4A373) : Colors.grey,
                              ),
                              onPressed: () => _toggleBookmark(currentItem),
                            ),
                          ],
                        ),
                        const SizedBox(height: 24),

                        // نص الآية بالخط الأميري
                        Text(
                          '﴿ ${currentItem.ayahText} ﴾',
                          textAlign: TextAlign.center,
                          style: GoogleFonts.amiri(
                            fontSize: 24,
                            height: 2.1,
                            fontWeight: FontWeight.bold,
                            color: const Color(0xFF2C3E50),
                          ),
                        ),
                        const SizedBox(height: 24),
                        const Divider(color: Color(0xFFF0ECE1), thickness: 1.2),
                        const SizedBox(height: 16),

                        // الوقفة التدبرية
                        const Row(
                          children: [
                            Icon(Icons.lightbulb_outline, color: Color(0xFFD4A373), size: 20),
                            SizedBox(width: 8),
                            Text(
                              'وقفة تدبرية',
                              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Color(0xFF1B4332)),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Text(
                          currentItem.reflection,
                          style: const TextStyle(fontSize: 15, height: 1.8, color: Color(0xFF4A5568)),
                        ),
                        const SizedBox(height: 20),

                        // العمل بالآية
                        const Row(
                          children: [
                            Icon(Icons.task_alt, color: Color(0xFF2D6A4F), size: 20),
                            SizedBox(width: 8),
                            Text(
                              'العمل بالآية',
                              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Color(0xFF1B4332)),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Text(
                          currentItem.actionPoint,
                          style: const TextStyle(fontSize: 14, height: 1.7, color: Color(0xFF2D6A4F)),
                        ),
                      ],
                    ),
                  ),
                ),
              ),

              const SizedBox(height: 16),

              // أزرار التحكم السفلية
              Row(
                children: [
                  // زر المشاركة
                  IconButton.filledTonal(
                    style: IconButton.styleFrom(
                      padding: const EdgeInsets.all(16),
                      backgroundColor: Colors.white,
                    ),
                    onPressed: () {
                      Share.share(
                        '﴿ ${currentItem.ayahText} ﴾ [سورة ${currentItem.surahName}: ${currentItem.ayahNumber}]\n\nوقفة تدبرية:\n${currentItem.reflection}\n\nتطبيق تدبر القرآن الكريم',
                      );
                    },
                    icon: const Icon(Icons.share_outlined, color: Color(0xFF1B4332)),
                  ),
                  const SizedBox(width: 12),

                  // زر التالي
                  Expanded(
                    child: ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF1B4332),
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 16),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                      ),
                      onPressed: _nextItem,
                      icon: const Icon(Icons.arrow_back_ios_new, size: 18),
                      label: const Text('آية تدبر تالية', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}