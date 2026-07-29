# Katman 0 — Yöntem seçici: kazanım → paket(ler) + kaplama(lar)

**Katman haritası:** Katman 0 = bu seçici (yöntemi SEÇER) · Katman 1 = `core/` çekirdek kuralları
(her yöntemde geçerli, sıra dayatmaz) · Katman 2 = `overlays/` kaplamaları (yönteme dik kaygılar) ·
Katman 3 = `pedagogy/` yöntem paketleri (sıra dayatan fazlı yapılar). Bu belge Katman 0'dır:
paketlerden **kimlikleriyle** söz eder, hiçbir paketin faz adını içermez ve Katman 1 kurallarını
esnetmez.

**Ne zaman:** Eğitim Okuması (SKILL.md Bölüm 0) beyan edildikten sonra, taslak (outline)
çizilmeden ÖNCE. Yöntem seçimi örtük kalamaz — v1'in "her konu aynı iskelete" tekdüzeliği tam
olarak bu adımın yokluğuydu.

## Girdiler

**Kazanım TÜRÜ** (her ölçülebilir hedef için ayrı belirle — 7 tür):

| Tür | Tanım (tek cümle) |
|---|---|
| `olgu` | Doğru/yanlış diye doğrulanabilir tekil bilgi (tarih, eşik değeri, kural metni). |
| `kavram` | Sınıflandırma yetisi: yeni örneği "bu X'tir / değildir" diye ayırt etme. |
| `prosedür` | Sıralı adımların doğru icrası (araç kullanımı, form süreci, raporlama akışı). |
| `ilke` | Neden-sonuç ilişkisini yeni duruma uygulama ("basınç artarsa ne olur?"). |
| `problem çözme` | Bilinen tek çözüm yolu olmayan durumda strateji kurma ve savunma. |
| `tutum` | Değer/tercih değişimi: kişinin bir davranışı *seçme* eğilimi. |
| `psikomotor` | Fiziksel/kas-hafızalı beceri ya da zaman baskılı akıcı icra. |

**Diğer 5 girdi:**

1. `PRIOR_KNOWLEDGE` (1–10) — yöntem kadranı, tanımı SKILL.md'de. Seçicinin en güçlü girdisi
   (uzmanlık-tersinme etkisi: yüksek önbilgide çözümlü örnek dozu düşer, problem-önce öne geçer).
2. **Hata maliyeti** (`düşük` | `orta` | `yüksek`) — öğrenen sahada yanılırsa bedeli ne? Yüksek
   maliyet keşif/deneme yöntemlerini pahalılaştırır, gösterim + kılavuzlu pratiği öne çeker.
3. **Zaman bütçesi** (dk) — dar bütçe (≤ 5 dk) çok-fazlı döngü paketlerini eler.
4. **Platform yetenekleri** — hangi ekran tipleri/araçlar mevcut (`simulation`, `game`,
   `adaptive_practice`, TTS, video…). Paketin `requires_platform` beyanıyla karşılaştırılır.
5. **Bağlam** — zorunlu/uyum mu gönüllü mü; kitle; kurum kısıtları; Eğitim Okuması'nın baskın
   modu (`keşif` | `gösterim` | `uygulama` | `değerlendirme`) burada sinyaldir: sağ-kalanlar
   arasında baskın moda yakın paketi öne alır, ama tek başına paket seçmez/elemez.

## Karar kaydı (B1 needs-decision çözümü) — KARAR ÖNERİSİ

**Benimsenen mekanizma: LLM muhakemesi + deterministik UYUMLULUK elemesi (hibrit).**

1. **Sert kısıt elemesi (deterministik, pazarlıksız):** her paket, ön-maddesinde
   (`references/pedagogy/_SCHEMA.md`) `outcome_types`, `prior_knowledge` (aralık), `error_cost`,
   `requires_platform` beyan eder. Kazanımın türü paket `outcome_types`'ında yoksa, PK değeri
   aralık dışındaysa, hata maliyeti düzeyi kapsanmıyorsa ya da platform şartı karşılanmıyorsa
   paket **elenir**. Eleme tartışmaya kapalıdır.
2. **Gerekçeli seçim (LLM muhakemesi):** sağ-kalanlar arasında skill'i okuyan model bağlamı
   (zaman bütçesi, baskın mod, kitle, kurum kısıtı) tartarak seçer ve gerekçesini **zorunlu**
   kaydeder (aşağıdaki çıktı biçimi + pre-flight Madde 1b).
3. **Son karar yazarındır (ajanın):** otomatik/mekanik son seçim yok; birden çok paket
   önerildiğinde seçimi gerekçesiyle yazar yapar. Gerekçesiz seçim = ihlal.

**Değerlendirilen alternatifler ve neden reddedildiği:**
- *Salt deterministik karar tablosu:* girdi kombinasyonları patlar ve tablo bağlamı (kitle,
  kurum, anlatı) tartamaz — tekdüzeliği başka biçimde yeniden üretir.
- *Ağırlıklı puanlama:* ağırlıklar keyfîdir; sayısal skor sahte kesinlik üretir ve gerekçeyi
  "puan öyle dedi"ye indirger.
- *Salt LLM muhakemesi:* kısıtsız gerekçe her paketi "savunabilir"; denetlenebilir değildir.
  Sert kısıtlar LLM'i dürüst tutar, LLM de tabloyu bağlama bağlar — ikisi birbirinin panzehiri.

> Bu bölüm bir **öneridir**; PR'da kullanıcı onayına sunulur (needs-decision etiketi).

## Örnek eşlemeler (eleme sonrası tipik sağ-kalanlar; `|` = gerekçeyle ikisinden biri)

| # | Girdi profili | → Paket(ler) | + Kaplama(lar) | Gerekçe (tek cümle) |
|---|---|---|---|---|
| 1 | prosedür · PK düşük (≤3) · hata maliyeti yüksek | `rosenshine-di` \| `4cid` | `cognitive-load` | Düşük önbilgide çözümlü örnek + kılavuzlu uygulama en güvenli yoldur; yüksek hata maliyeti keşif denemesini pahalı kılar. |
| 2 | kavram · PK orta (4–6) · hata maliyeti düşük | `5e-inquiry` \| `productive-failure` | — | Düşük hata maliyeti güvenli keşfe/üretken boğuşmaya alan açar; orta önbilgi çürütülecek ön-kavram malzemesi sağlar. |
| 3 | problem çözme · PK yüksek (≥7) | `pbl-case` | `expertise-adaptive` | Yüksek önbilgide gösterim dozu zarar verebilir (uzmanlık tersinmesi); gerçekçi vaka problem-önce çalışır. |
| 4 | mevzuat/uyum (olgu+prosedür) · zorunlu eğitim bağlamı | `gagne-9` + `mastery-learning` | `assessment-alignment` | Uyum eğitimi tam kapsama ister: dokuz-olay yapısı içeriği, tam-öğrenme döngüsü eşiği garanti eder (paket bileşimi: çakışma beyanı yoksa serbest). |
| 5 | tutum | `kolb-experiential` | `arcs` | Tutum bilgi aktarımıyla değil deneyim+yansıtma döngüsüyle değişir; ARCS ilgililiği ve güveni taşır. |
| 6 | olgu ağırlıklı hızlı tazeleme · PK yüksek · dar zaman bütçesi | `retrieval-spaced` | — | Bilinen olguların kalıcılığı yeniden-anlatımla değil geri-getirme pratiğiyle sağlanır; dar bütçede en yüksek getiri. |
| 7 | psikomotor/prosedür · hata maliyeti yüksek · platformda simülasyon var | `sim-drill` | `accessibility` | Akıcı icra ancak tekrarlı, güvenli tatbikatla oturur; simülasyon platform şartıdır (`requires_platform`). |

## Çoklu kazanım, çoklu paket

- **Kazanım başına seçim yapılır.** Bir kurs birden çok kazanım taşıyorsa kazanımlar farklı
  paketlere düşebilir (örn. O1 prosedür → `rosenshine-di`, O2 tutum → `kolb-experiential`).
  Paketlerin `conflicts_with (kapsamı HEDEFTİR — aynı hedefte yasak, farklı hedeflerde serbest; bkz. pedagogy/_SCHEMA.md)` beyanları çakışıyorsa aynı kursta birleştirilemez — kursu böl
  ya da tek pakete karar ver (gerekçeyle).
- **Hiçbir paket kanonik/varsayılan-dayatmalı değildir.** Seçici önerir; "her kurs X paketi"
  kuralı yoktur.
- **Hiçbir paket uymadıysa (tümü elendiyse):** belgeli varsayılan **`gagne-9`**'dur (en geniş
  kazanım-türü kapsamı, platform şartı yok) — ama varsayılana düşmek **zorunlu gerekçe** ister:
  çıktı beyanına "hiçbir paket kısıtları karşılamadı, çünkü …" cümlesi yazılır. Varsayılan ≠
  kanonik; yalnız eleme boş küme döndürdüğünde ve gerekçeyle kullanılır.

## Belirsiz / eksik girdi için varsayılan davranış

| Eksik girdi | Varsayılan | Not |
|---|---|---|
| PRIOR_KNOWLEDGE | **3 varsay** (acemi-eğilimli) ve beyan et | Acemiye fazla gösterim, uzmana eksik gösterimden daha az zarar verir. |
| Hata maliyeti | `orta`; uyum/sağlık/güvenlik bağlamında `yüksek` | Sessiz `düşük` varsayma — keşif yöntemini yanlışlıkla ucuzlatır. |
| Zaman bütçesi | Mikroöğrenme 3–8 dk | SKILL.md workflow 1 ile aynı. |
| Platform | 28 çekirdek ekran tipi var, ek araç yok varsay | `requires_platform` beyan eden paketleri eler; elemeyi çıktıda listele. |
| Kazanım türü çıkarılamıyor | **TEK soru sor** (Bölüm 0 kuralı) | Tür seçicinin birincil anahtarıdır; tahminle geçilmez. |

Varsayılan kullandıysan çıktı beyanında işaretle — sessiz varsayılan = ihlal.

## Çıktı biçimi (B3 pack kimlikleriyle uyumlu — YÖNTEM BEYANI)

```text
YÖNTEM BEYANI (kurs briefine / pre-flight Madde 1b'ye yazılır)
- kazanım: O1 (tür: prosedür · PK: 3 · hata maliyeti: yüksek · bütçe: 6 dk)
  paket: rosenshine-di                      # references/pedagogy/ pack kimliği
  kaplamalar: [cognitive-load, accessibility]
  elenenler: [productive-failure (error_cost uyumsuz), sim-drill (requires_platform karşılanmadı)]
  gerekçe: "Kitle ilk kez görüyor ve sahada yanlış rapor geri alınamıyor; kılavuzlu
  uygulamalı doğrudan öğretim, keşif denemesinden daha güvenli."
```

Geçerli **paket kimlikleri** (Katman 3, `references/pedagogy/` — C1–C12): `rosenshine-di`,
`merrill-fpi`, `5e-inquiry`, `4cid`, `mastery-learning`, `productive-failure`, `pbl-case`,
`kolb-experiential`, `sim-drill`, `gagne-9`, `cognitive-apprenticeship`, `retrieval-spaced`.
Geçerli **kaplama kimlikleri** (Katman 2, `references/overlays/` — D1–D6): `cognitive-load`,
`udl`, `arcs`, `expertise-adaptive`, `assessment-alignment`, `accessibility`.

## Katman 1 ile ilişki (değişmez)

Seçici hangi paketi seçerse seçsin Katman 1 aynen geçerlidir: kanıt bağlama (K1–K5), hiza
(H1–H3), feedback anatomisi (G1–G3), skorlama zamanlaması (Z1–Z3). Paketin kanıt üreten faz(lar)ı
ön-maddesindeki `evidence_phase`/`evidence_phases` beyanıdır (çoğul olabilir); soru-düzeyi bağ
ise HER ZAMAN çoğuldur (`evidence_screen_ids` — bir soru birden çok kanıt kaynağına yaslanabilir).
