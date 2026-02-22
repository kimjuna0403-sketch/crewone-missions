"""
STEP 2: 초기 데이터 세팅 스크립트 (1회만 실행)
- crews 30개 INSERT
- crew_reward_schedule 생성 (30개 크루 × 30일 = 900개 행)
"""

import json
from supabase import create_client

# ────────────────────────────
# 여기에 본인 Supabase 정보 입력
SUPABASE_URL = "https://fivzbxxeactbtmimjhvh.supabase.co"
SUPABASE_KEY = "sb_publishable_UOF0tsAEcbNUKj2ZCYEctg_q21twRLt"
# ────────────────────────────

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ── 1. 크루 30개 ──────────────────────────────────────────
CREWS = [
    {"crew_id": "CREW_EX_01", "crew_name": "퇴근 후 번아웃 탈출 러닝단", "crew_goal": "평일 저녁 30분 러닝을 주 3회 인증해 스트레스 해소 루틴 만들기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_EX_02", "crew_name": "주말 리프레시 5천보단", "crew_goal": "주말 5천보 걷기를 인증해 가벼운 활동 습관 만들기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_EX_03", "crew_name": "집콕 10분 리셋 스트레칭단", "crew_goal": "집에서 10분 스트레칭을 꾸준히 인증해 몸 컨디션 리셋하기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_EX_04", "crew_name": "7일 홈트 부트캠프단", "crew_goal": "7일 홈트 미션을 매일 체크인해 운동 루틴을 시작하기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_EX_05", "crew_name": "헬스장 입문 루틴클럽", "crew_goal": "헬스장 기본 루틴을 주 2~3회 실행해 근력운동 습관 만들기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_EX_06", "crew_name": "생활 속 걷기 업그레이드단", "crew_goal": "일상 속 걷기를 늘리고 수시 인증해 활동량 업그레이드하기", "topic": "운동/활동", "is_custom": False},
    {"crew_id": "CREW_DI_07", "crew_name": "평일 집밥 지킴이단", "crew_goal": "평일 집밥 중심 식사를 인증해 식생활 균형 잡기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_DI_08", "crew_name": "배달 브레이크 챌린지단", "crew_goal": "배달 횟수를 줄이는 습관 미션을 실천해 소비·식단 정돈하기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_DI_09", "crew_name": "외식 스마트 초이스단", "crew_goal": "외식 시 메뉴 선택 기준을 적용해 더 건강한 선택을 실천하기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_DI_10", "crew_name": "간식 리셋 프로젝트단", "crew_goal": "간식 패턴을 점검하고 대체 간식으로 바꾸는 미션 수행하기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_DI_11", "crew_name": "하루 1.5L 워터 챌린지단", "crew_goal": "하루 물 1.5L 섭취를 인증해 컨디션 관리 루틴 만들기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_DI_12", "crew_name": "주말 식단 리셋 클럽", "crew_goal": "주말 식단을 정리·리셋해 다음 주를 가볍게 시작하기", "topic": "다이어트/식생활", "is_custom": False},
    {"crew_id": "CREW_RT_13", "crew_name": "아침 20분 스타트업단", "crew_goal": "아침 20분 고정 루틴을 체크인해 하루 시작을 안정화하기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_RT_14", "crew_name": "30일 습관 완성 프로젝트", "crew_goal": "30일 동안 목표 습관 1개를 매일 체크인해 완성하기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_RT_15", "crew_name": "수면 밸런스 회복단", "crew_goal": "수면 루틴 미션으로 취침·기상 리듬을 회복하기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_RT_16", "crew_name": "퇴근 후 10분 정리클럽", "crew_goal": "퇴근 후 10분 정리 미션을 인증해 집·마음 정돈하기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_RT_17", "crew_name": "주간 3목표 달성단", "crew_goal": "주간 목표 3개를 세우고 달성 체크로 성취 루틴 만들기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_RT_18", "crew_name": "밤 1시간 디지털 OFF단", "crew_goal": "밤 1시간 디지털 디톡스를 실천해 휴식 몰입도 높이기", "topic": "루틴/자기관리", "is_custom": False},
    {"crew_id": "CREW_BE_19", "crew_name": "7일 피부 루틴 챌린지", "crew_goal": "7일 스킨케어 루틴을 매일 인증해 피부 컨디션 안정화하기", "topic": "뷰티/케어", "is_custom": False},
    {"crew_id": "CREW_BE_20", "crew_name": "데일리 선·클렌징 고정단", "crew_goal": "선케어·클렌징을 매일 고정 루틴으로 만들어 꾸준히 실천하기", "topic": "뷰티/케어", "is_custom": False},
    {"crew_id": "CREW_BE_21", "crew_name": "보습 밸런스 유지단", "crew_goal": "바디 보습 루틴을 인증해 건조 스트레스 줄이기", "topic": "뷰티/케어", "is_custom": False},
    {"crew_id": "CREW_BE_22", "crew_name": "주2회 뷰티 리마인드단", "crew_goal": "주 2회 뷰티 미션을 수행해 케어 습관 유지하기", "topic": "뷰티/케어", "is_custom": False},
    {"crew_id": "CREW_EC_23", "crew_name": "에코 장바구니 실천단", "crew_goal": "장바구니 사용을 인증해 일회용품 사용을 줄이기", "topic": "친환경/소비습관", "is_custom": False},
    {"crew_id": "CREW_EC_24", "crew_name": "주1회 리필 습관단", "crew_goal": "주 1회 리필/리유즈 행동을 실천해 소비 습관 바꾸기", "topic": "친환경/소비습관", "is_custom": False},
    {"crew_id": "CREW_EC_25", "crew_name": "분리배출 마스터단", "crew_goal": "분리배출 미션을 인증해 집에서 지속 가능한 습관 만들기", "topic": "친환경/소비습관", "is_custom": False},
    {"crew_id": "CREW_EC_26", "crew_name": "탄소 절감 루틴 프로젝트", "crew_goal": "탄소 절감 행동을 루틴화해 친환경 생활을 유지하기", "topic": "친환경/소비습관", "is_custom": False},
    {"crew_id": "CREW_CT_27", "crew_name": "주말 1편 완주클럽", "crew_goal": "주말에 콘텐츠 1편을 완주하고 기록해 소소한 성취 만들기", "topic": "콘텐츠/집콕", "is_custom": False},
    {"crew_id": "CREW_CT_28", "crew_name": "출퇴근 20분 콘텐츠단", "crew_goal": "출퇴근 20분 콘텐츠 소비를 루틴화해 꾸준히 즐기기", "topic": "콘텐츠/집콕", "is_custom": False},
    {"crew_id": "CREW_CT_29", "crew_name": "콘텐츠 큐레이션단", "crew_goal": "주 1회 콘텐츠를 추천·정리해 취향 큐레이션 습관 만들기", "topic": "콘텐츠/집콕", "is_custom": False},
    {"crew_id": "CREW_CT_30", "crew_name": "취침 전 15분 힐링시청단", "crew_goal": "취침 전 15분 힐링 콘텐츠를 매일 실행해 수면 전 루틴 만들기", "topic": "콘텐츠/집콕", "is_custom": False},
]

# ── 2. day_number → tier 매핑 ──────────────────────────────
def get_tier(day_number: int) -> int:
    if day_number <= 6:
        return 1
    elif day_number <= 13:
        return 2
    elif day_number <= 20:
        return 3
    elif day_number <= 29:
        return 4
    else:
        return 5

# ── 3. reward_master 로드 ─────────────────────────────────
with open("reward_master_v1_200.json", "r", encoding="utf-8") as f:
    REWARD_MASTER = json.load(f)

def get_reward(topic: str, tier: int) -> dict:
    """topic + tier 맞는 첫 번째 보상 반환"""
    for r in REWARD_MASTER:
        if r["topic"] == topic and r["tier"] == tier:
            return r
    # fallback: topic 무시하고 tier만 매칭
    for r in REWARD_MASTER:
        if r["tier"] == tier:
            return r
    return None

# ── 4. 실행 ───────────────────────────────────────────────
def main():
    # crews INSERT
    print("크루 30개 INSERT 중...")
    res = supabase.table("crews").upsert(CREWS).execute()
    print(f"  완료: {len(CREWS)}개")

    # crew_reward_schedule INSERT
    print("보상 스케줄 생성 중 (30크루 × 30일 = 900개)...")
    schedule_rows = []
    for crew in CREWS:
        for day in range(1, 31):
            tier = get_tier(day)
            reward = get_reward(crew["topic"], tier)
            if reward:
                schedule_rows.append({
                    "crew_id": crew["crew_id"],
                    "day_number": day,
                    "tier": tier,
                    "reward_id": reward["reward_id"],
                    "reward_name": reward["reward_name"],
                    "reward_type": reward["reward_type"],
                    "amount_point": reward.get("amount_point"),
                })

    # 100개씩 나눠서 INSERT (Supabase 제한)
    chunk_size = 100
    for i in range(0, len(schedule_rows), chunk_size):
        chunk = schedule_rows[i:i+chunk_size]
        supabase.table("crew_reward_schedule").upsert(chunk).execute()
        print(f"  {i + len(chunk)}/{len(schedule_rows)} 완료")

    print("\n✅ 초기 데이터 세팅 완료!")
    print(f"  - crews: {len(CREWS)}개")
    print(f"  - crew_reward_schedule: {len(schedule_rows)}개")

if __name__ == "__main__":
    main()
