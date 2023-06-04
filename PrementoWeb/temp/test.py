from hanspell import spell_checker

script = "사람들이 많이 말하지 않는 치포의 진실을 좀 알려 드리겠습니다 진실을 알고 싶으면 요런 문서 들여다 보시면 됩니다"
result = spell_checker.check(script)

print(result.checked)