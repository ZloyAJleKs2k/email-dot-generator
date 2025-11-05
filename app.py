import itertools


def generate_emails_with_dots(email: str, output_file: str, max_emails: int = 1000):
    if '@' not in email:
        raise ValueError("Некорректный email: отсутствует @")

    local, domain = email.split('@', 1)
    n = len(local)

    possible_positions = list(range(1, n))

    results = set()
    results.add(email)

    for num_dots in range(1, len(possible_positions) + 1):
        if len(results) >= max_emails:
            break
        for combo in itertools.combinations(possible_positions, num_dots):
            if len(results) >= max_emails:
                break
            new_local = list(local)
            for pos in sorted(combo, reverse=True):
                new_local.insert(pos, '.')
            new_email = ''.join(new_local) + '@' + domain
            results.add(new_email)

    results = list(results)[:max_emails]

    with open(output_file, 'w', encoding='utf-8') as f:
        for em in sorted(results):
            f.write(em + '\n')

    print(f"Сгенерировано {len(results)} email-адресов (максимум: {max_emails}). Сохранено в {output_file}")


if __name__ == "__main__":
    original_email = "yourgmail@gmail.com"
    output_file = "emails_with_dots_full.txt"
    max_count = 200
    generate_emails_with_dots(original_email, output_file, max_emails=max_count)