# -*- coding: utf-8 -*-
import os
from pathlib import Path

base = Path(os.environ.get("USERPROFILE", r"C:\\Users\\Default"))
path = base / "Desktop" / "TEST10" / "index.html"
text = path.read_text(encoding="utf-8", errors="ignore")

replacements = [
    ("Hello! We are good plan!", "ONEOFF | LED Rental"),
    ("good plan", "ONEOFF"),
    ("av-drop", "LED WALL"),
    ("best systems", "LED INFO DESK"),
    ("vomo", "LED BANNER"),
    ("audio/visual", "CUSTOM LED"),
    ("굿플랜 소개", "ONEOFF 소개"),
    ("포트폴리오 보기", "적용사례"),
    ("We Elevate Your Event Experience.", "폐기물 0%에 도전하는 지속 가능한 전시"),
    ("“good plan’은", "ONEOFF는"),
    ("지구환경", "LED 렌탈"),
    ("지속가능", "원스톱 운영"),
    ("한 이벤트 실천을 위한", "전시 렌탈을 위한"),
    ("코엑스의 프리미엄 이벤트 서비스", "ONEOFF의 LED 렌탈 솔루션"),
    ("전시 부스와 세미나장, VIP라운지", "LED WALL, LED 인포데스크, LED 배너,"),
    ("등의 시스템은", "Custom LED 렌탈까지"),
    ("친환경, 비용절감, 그리고 고품격 이벤트 구현", "출력물 없이 빠르고 안정적으로"),
    ("을 위해 디자인 되었습니다.", "운영합니다."),
    ("AV-Drop", "LED WALL"),
    ("친환경 무대백드롭 시스템", "메인 무대와 백월에 최적화된 대형 LED WALL 렌탈."),
    ("Reusable Modular Stage Backdrop", "Large LED Wall Rental"),
    ("LED UP", "LED INFO DESK"),
    ("친환경 라이팅월 시스템", "브랜드 메시지를 가장 먼저 전달하는 LED 인포데스크 렌탈."),
    ("Sustainable Lighting Wall", "LED Info Desk Rental"),
    ("Vomo", "LED BANNER"),
    ("친환경 모듈부스 시스템", "동선을 따라 메시지를 이어주는 대형 LED 배너 렌탈."),
    ("Eco-Friendly Lightweight Booth", "LED Banner Rental"),
    ("WallStack", "Custom LED"),
    ("친환경 파티션 월 시스템", "공간 높이를 살리는 Custom LED 렌탈로 포인트를 강조합니다."),
    ("Modular Partition Wall System", "Custom LED Rental"),
    ("THE GREENER CHOICE", "SUSTAINABLE EXHIBITION"),
    ("굿플랜을 통해 친환경 자재 및 시스템을 이용한 행사에 대해,  행사 종료 후", "출력물 대신 LED로, 버려지는 전시를 줄입니다."),
    ("탄소 절감량을 수치화한 인증서 및 리포트", "콘텐츠는 바뀌어도, 구조는 남습니다."),
    ("를 발행해드립니다.", "친환경 전시 가이드에 대응 가능한 LED 솔루션."),
    ("이제는 단순한", "출력물 ZERO 전시"),
    ("‘친환경 행사’", "종이 없는 전시, 디지털 전시"),
    ("에서 나아가, 실제 절감 효과를 수치로 증빙하고,", "프레임 모듈화로 반복 사용합니다."),
    ("지속가능성 실천", "지속 가능한 전시"),
    ("을 이해관계자와 공유할 수 있는 자료로 활용하세요.", "ESG·친환경 전시 대응"),
    ("탄소 절감 인증서 및 보고서 신청방법", "렌탈 프로세스"),
    ("굿플랜 이용 시,  행사 전 또는 행사 종료 후", "문의부터 납품, 설치, 회수까지 빠르게 진행합니다."),
    ("7일 이내", "01 렌탈 문의"),
    ("에 담당자에게 요청하시면  검토 후 발행해 드립니다.", "02 스펙 확인 · 03 배송/설치 · 04 운영/회수"),
    ("2024년 굿플랜 성과", "렌탈 운영 지표"),
    ("탄소 절감 성과 요약 (연간)", "정시 납품, 장비 가동률, 빠른 응대로"),
    ("총 감축 탄소량", "정시 납품"),
    ("1,598,831 kgCO₂e", "98%"),
    ("목공 장치 사용 대비 탄소 절감률", "장비 가동률"),
    ("91%", "99.5%"),
    ("탄소 절감 지표", "현장 응답"),
    ("나무 185,911그루를 심은 것과 동일한 CO₂ 흡수 효과", "1h"),
    ("빙하 4,264㎡의 융해 방지", "재렌탈률"),
    ("53,294,362개의 풍선 부피에 해당하는 CO₂ 절감", "72%"),
    ("자동차 주행 거리 819,913km 이동 가능", "안정적인 렌탈 운영"),
    ("출처", "렌탈 문의"),
    ("Affiliated Organizations of Korea Forest Service", "stagemonster@naver.com"),
    ("Based on study from lead author Dirk Notz from Max Planck Institute", "010-5632-5042"),
    ("The CSCT of the University of Bath", "경기도 김포시 양촌읍 유현리 171-3"),
    ("Ministry of Environment", "MON-SAT 09:00~18:00"),
    ("굿플랜 적용 시스템", "렌탈 서비스"),
    ("AV-Drop (모듈 백드롭)", "LED WALL"),
    ("7,695 ㎡", "대형 사이즈 모듈 구성"),
    ("LED UP(모듈 라이팅 월)", "LED 인포데스크"),
    ("4,191 ㎡", "맞춤 사이즈/형태 제작"),
    ("Vomo(모듈 친환경 부스)", "LED 배너"),
    ("8,520 m", "장거리 시인성 최적화"),
    ("굿플랜 시스템별 탄소절감 비교", "Custom LED"),
    ("탄소 배출 산정 방식", "공간 높이를 살리는 Custom LED 렌탈"),
    ("본 연구는 1회 부스 설치·운영을 기준으로 good plan 자재와 목공 장치를 비교하였다.", "공간 구조에 맞춘 배열"),
    ("시스템 경계 :", "브랜드 컬러/패턴 연동"),
    ("원자재 생산부터 폐기까지 전 과정(cradle to grave) 포함.", "안전 규격 설치 진행"),
    ("산정 방식 :", "콘텐츠 송출 세팅"),
    ("good plan 자재는 30회 재사용 후 폐기, 목공 부스는 1회 사용 후 폐기 가정. 총 배출량을 1회 사용 기준으로 환산해 비교.", "맞춤형 설계로 현장 포인트 강조"),
    ("비교 대상 :", "LED 렌탈 원스톱 지원"),
    ("목공 부스는 낙엽송 기준, 동일 부피 기준으로 무게 및 탄소배출량 산정.", "설치/철거 원스톱 지원"),
    ("운송 가정 :", "현장 일정에 맞춘 빠른 납품"),
    ("good plan은 코엑스 내 보관, 운송 없음 처리. 목공은 가장 가까운 업체 기준 거리 적용.", "전지역 렌탈 가능"),
    ("전력 사용 :", "맞춤 콘텐츠 운영"),
    ("1회 사용 시 8시간 기준, 조명 등 전력량 산정.", "전문 설치팀 운영"),
    ("폐기 처리 :", "안정적인 장비 관리"),
    ("2023년 통계 기준, 재활용/소각/매립 비율 반영하여 배출계수 적용.", "고해상도 브랜드 송출"),
    ("가볍게 설치하고, 공간은 효율적으로!", "단한번의 특별한 경험"),
    ("굿플랜은 품질과 환경, 그리고 운영의 편리함까지 생각한 이벤트 솔루션입니다.", "ONEOFF LED렌탈 솔루션"),
    ("지금, 지속 가능한 방식으로 더 나은 경험을 만들어보세요!", "지금, ONEOFF와 함께 전시를 준비하세요!"),
    ("굿플랜 서비스 문의처", "렌탈 문의"),
    ("goodplan@coex.co.kr", "stagemonster@naver.com"),
    ("02-6000-1151 / 1363 / 1157 / 1365", "010-5632-5042"),
]

missing = []
for old, new in replacements:
    if old not in text:
        missing.append(old)
    else:
        text = text.replace(old, new)

path.write_text(text, encoding="utf-8")

if missing:
    print("Missing:")
    for item in missing:
        print(item)
else:
    print("All replacements applied.")
