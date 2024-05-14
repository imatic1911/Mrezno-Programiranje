import dns.resolver

def dns_lookup(query, record_type):
    try:
        result = dns.resolver.resolve(query, record_type)
        if record_type == 'A':
            print("IP adresa za", query, "je:")
            for ip in result:
                print(ip.to_text())
        elif record_type == 'MX':
            print("MX zapisi za", query, "su:")
            for mx in result:
                print(mx.to_text())
        elif record_type == 'PTR':
            print("PTR zapis za", query, "je:")
            for ptr in result:
                print(ptr.to_text())
    except dns.resolver.NoAnswer:
        print("Nema rezultata za upit", query)
    except dns.resolver.NXDOMAIN:
        print("Ne postoji zapis za domenu", query)
    except Exception as e:
        print("Došlo je do pogreške:", e)

# Primjeri upita
queries = [
    ("www.google.com", "A"),
    ("gmail.com", "MX"),
    ("8.8.8.8", "PTR")
]

# Izvršavanje upita
for query, record_type in queries:
    print("=" * 50)
    print("Izvršavanje upita za:", query)
    dns_lookup(query, record_type)
