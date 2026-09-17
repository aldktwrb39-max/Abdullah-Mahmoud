import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/tadabbur_model.dart';

class QuranService {
  // مثال لجلب آية محددة بالرسم العثماني
  // Al-Quran Cloud API مجاني ومستقر جداً
  static Future<String> fetchAyahText(int surah, int ayah) async {
    final url = Uri.parse('https://api.alquran.cloud/v1/ayah/$surah:$ayah/quran-uthmani');
    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return data['data']['text'];
      }
    } catch (e) {
      print('Error fetching ayah: $e');
    }
    return '';
  }

  // محتوى تدبري أولي وموثوق (يمكن ربطه لاحقاً بـ Supabase أو Firebase خاص بك)
  static List<TadabburItem> getSampleItems() {
    return [
      TadabburItem(
        id: 1,
        surahName: 'البقرة',
        ayahNumber: 152,
        ayahText: 'فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ',
        reflection: 'لو لم يكن للذكر من جزاء إلا أن يذكرك ملك الملوك في ملأ خير من ملئك لكفى به شرفاً وسكينة لقلبك في زحام الدنيا.',
        actionPoint: 'اجعل لسانك رطباً بالتسبيح والاستغفار في أوقات الانتظار اليوم.',
      ),
      TadabburItem(
        id: 2,
        surahName: 'الرعد',
        ayahNumber: 28,
        ayahText: 'الَّذِينَ آمَنُوا وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ اللَّهِ ۗ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ',
        reflection: 'القلب مخلوق لا يسكن لقريب ولا بعيد، ولا لمال ولا ولد، إلا إذا اتصل بمصدر الأمان المطلق وخالقه سبحانه.',
        actionPoint: 'كلما شعرت بتشتت أو ضيق اليوم، أوقف كل شيء دقيقة وردد: لا حول ولا قوة إلا بالله بحضور قلب.',
      ),
      TadabburItem(
        id: 3,
        surahName: 'الضحى',
        ayahNumber: 3,
        ayahText: 'مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ',
        reflection: 'انقطاع الوحي لم يكن هجراناً، بل إعداداً لفيض أكبر. وتأخر الفرج في حياتك ليس إهمالاً، بل تهيئة لخير لم تكن لتبلغه دونه.',
        actionPoint: 'حسن الظن بالله عند تأخر مطلوبك، وتذكر لطفه الخفي في كل ما فات.',
      ),
    ];
  }
}