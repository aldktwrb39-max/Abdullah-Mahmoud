class TadabburItem {
  final int id;
  final String ayahText;
  final String surahName;
  final int ayahNumber;
  final String reflection; // الوقفة التدبرية
  final String actionPoint; // العمل بالآية
  bool isBookmarked;

  TadabburItem({
    required this.id,
    required this.ayahText,
    required this.surahName,
    required this.ayahNumber,
    required this.reflection,
    required this.actionPoint,
    this.isBookmarked = false,
  });

  // للتحويل والتخزين المحلي في Hive
  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'ayahText': ayahText,
      'surahName': surahName,
      'ayahNumber': ayahNumber,
      'reflection': reflection,
      'actionPoint': actionPoint,
      'isBookmarked': isBookmarked,
    };
  }

  factory TadabburItem.fromMap(Map<dynamic, dynamic> map) {
    return TadabburItem(
      id: map['id'] ?? 0,
      ayahText: map['ayahText'] ?? '',
      surahName: map['surahName'] ?? '',
      ayahNumber: map['ayahNumber'] ?? 0,
      reflection: map['reflection'] ?? '',
      actionPoint: map['actionPoint'] ?? '',
      isBookmarked: map['isBookmarked'] ?? false,
    );
  }
}