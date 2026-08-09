const teltools = require("./teltools_block.js");

var DIG={dev:"०१२३४५६७८९",tel:"౦౧౨౩౪౫౬౭౮౯"}, AVA={dev:"ऽ",tel:"ఽ"};
function prep(s){return s.replace(/-/g,"").replace(/ḷ/g,"ḻ");}
function post(s,sc){s=s.replace(/\|\|/g,"॥").replace(/\|/g,"।").replace(/['’]/g,AVA[sc]).replace(/[0-9]/g,function(d){return DIG[sc][+d];});if(sc==="dev")s=s.replace(/(^|[\s।॥])ओं(?=$|[\s।॥])/g,"$1ॐ");return s;}
function toDev(i){return post(teltools.tel2hin(teltools.iast2tel(prep(i))),"dev");}
var SVARA={"_":"॒","^":"॑"};
function devSvara(iast){var out="",re=/[_^]/g,last=0,m;while((m=re.exec(iast))){out+=toDev(iast.slice(last,m.index))+SVARA[m[0]];last=m.index+1;}out+=toDev(iast.slice(last));return out.replace(/([॒॑])([ःं])/g,"$2$1");}

// [iast_a, iast_b, source_a_raw, source_b_raw] per verse, straight from
// tools/stotras/eval-nsw.py padas (with the trailing " |"/num stripped back
// off before rendering, matching how the raw wikitext line looked before
// dev2iast+conv touched it) vs. the raw wikitext accented lines.
const cases = [
  // verse 1
  ["nāsa^dāsī_nno sadā^sītta_dānīṃ_ nāsī_drajo_ no vyo^mā pa_ro yat",
   "नास॑दासी॒न्नो सदा॑सीत्त॒दानीं॒ नासी॒द्रजो॒ नो व्यो॑मा प॒रो यत्"],
  ["kimāva^rīvaḥ_ kuha_ kasya_ śarma_nnambhaḥ_ kimā^sī_dgaha^naṃ gabhī_ram",
   "किमाव॑रीवः॒ कुह॒ कस्य॒ शर्म॒न्नम्भः॒ किमा॑सी॒द्गह॑नं गभी॒रम्"],
  // verse 2
  ["na mṛ_tyurā^sīda_mṛtaṃ_ na tarhi_ na rātryā_ ahna^ āsītprake_taḥ",
   "न मृ॒त्युरा॑सीद॒मृतं॒ न तर्हि॒ न रात्र्या॒ अह्न॑ आसीत्प्रके॒तः"],
  ["ānī^davā_taṃ sva_dhayā_ tadekaṃ_ tasmā^ddhā_nyanna pa_raḥ kiṃ ca_nāsa^",
   "आनी॑दवा॒तं स्व॒धया॒ तदेकं॒ तस्मा॑द्धा॒न्यन्न प॒रः किं च॒नास॑"],
  // verse 3
  ["tama^ āsī_ttama^sā gū_ḷhamagre^'prake_taṃ sa^li_laṃ sarva^mā i_dam",
   "तम॑ आसी॒त्तम॑सा गू॒ळ्हमग्रे॑ऽप्रके॒तं स॑लि॒लं सर्व॑मा इ॒दम्"],
  ["tu_cchyenā_bhvapi^hitaṃ_ yadāsī_ttapa^sa_stanma^hi_nājā^ya_taika^m",
   "तु॒च्छ्येना॒भ्वपि॑हितं॒ यदासी॒त्तप॑स॒स्तन्म॑हि॒नाजा॑य॒तैक॑म्"],
  // verse 4
  ["kāma_stadagre_ sama^varta_tādhi_ mana^so_ retaḥ^ pratha_maṃ yadāsī^t",
   "काम॒स्तदग्रे॒ सम॑वर्त॒ताधि॒ मन॑सो॒ रेतः॑ प्रथ॒मं यदासी॑त्"],
  ["sa_to bandhu_masa^ti_ nira^vindanhṛ_di pra_tīṣyā^ ka_vayo^ manī_ṣā",
   "स॒तो बन्धु॒मस॑ति॒ निर॑विन्दन्हृ॒दि प्र॒तीष्या॑ क॒वयो॑ मनी॒षा"],
  // verse 5
  ["ti_ra_ścīno_ vita^to ra_śmire^ṣāma_dhaḥ svi^dā_sī3du_pari^ svidāsī3t",
   "ति॒र॒श्चीनो॒ वित॑तो र॒श्मिरे॑षाम॒धः स्वि॑दा॒सी३दु॒परि॑ स्विदासी३त्"],
  ["re_to_dhā ā^sanmahi_māna^ āsansva_dhā a_vastā_tpraya^tiḥ pa_rastā^t",
   "रे॒तो॒धा आ॑सन्महि॒मान॑ आसन्स्व॒धा अ॒वस्ता॒त्प्रय॑तिः प॒रस्ता॑त्"],
  // verse 6
  ["ko a_ddhā ve^da_ ka i_ha pra vo^ca_tkuta_ ājā^tā_ kuta^ i_yaṃ visṛ^ṣṭiḥ",
   "को अ॒द्धा वे॑द॒ क इ॒ह प्र वो॑च॒त्कुत॒ आजा॑ता॒ कुत॑ इ॒यं विसृ॑ष्टिः"],
  ["a_rvāgde_vā a_sya vi_sarja^ne_nāthā_ ko ve^da_ yata^ āba_bhūva^",
   "अ॒र्वाग्दे॒वा अ॒स्य वि॒सर्ज॑ने॒नाथा॒ को वे॑द॒ यत॑ आब॒भूव॑"],
  // verse 7
  ["i_yaṃ visṛ^ṣṭi_ryata^ āba_bhūva_ yadi^ vā da_dhe yadi^ vā_ na",
   "इ॒यं विसृ॑ष्टि॒र्यत॑ आब॒भूव॒ यदि॑ वा द॒धे यदि॑ वा॒ न"],
  ["yo a_syādhya^kṣaḥ para_me vyo^ma_nso a_ṅga ve^da_ yadi^ vā_ na veda^",
   "यो अ॒स्याध्य॑क्षः पर॒मे व्यो॑म॒न्सो अ॒ङ्ग वे॑द॒ यदि॑ वा॒ न वेद॑"],
];

let allOk = true;
cases.forEach(([iast, src], i) => {
  const rendered = devSvara(iast);
  const ok = rendered === src;
  if (!ok) allOk = false;
  console.log(`[${i}] ${ok ? "OK" : "MISMATCH"}`);
  if (!ok) {
    console.log("  src:      " + src);
    console.log("  rendered: " + rendered);
    // char diff
    const L = Math.max(src.length, rendered.length);
    for (let c = 0; c < L; c++) {
      if (src[c] !== rendered[c]) {
        console.log(`  first diff at char ${c}: src=${JSON.stringify(src[c])} (U+${src.charCodeAt(c)?.toString(16)}) rendered=${JSON.stringify(rendered[c])} (U+${rendered.charCodeAt(c)?.toString(16)})`);
        break;
      }
    }
  }
});
console.log(allOk ? "\nALL 14 LINES BYTE-EXACT MATCH" : "\nSOME MISMATCHES FOUND");
