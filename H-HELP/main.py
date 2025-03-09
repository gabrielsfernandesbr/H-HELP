import socket as sock
import whois as www
import phonenumbers as phone
from phonenumbers import geocoder, carrier, timezone, is_valid_number, is_possible_number
import ipaddress

def source_ip_info():
    try:
        url = input("Enter the domain address (e.g. www.example.com):")
        ip = sock.gethostbyname(url)
        
        print(f"\nIP address of {url}: {ip}")
    except Exception as error:
        print(f"Error: {error}")

def get_domain_info():
    try:
        domain_get = input("Enter the domain (e.g. example.com): ")
        query = www.whois(domain_get)
        
        print(f"\n=== WHOIS Query Result ===")
        print(f"Domain: {domain_get}")
        print(f"{'='*30}")
        print(f"WHOIS Information: ")
        print(f"{'='*30}")
        
        for key, value in query.items():
            print(f"{key}: {value}")
        
        print(f"\n{'='*30}")
        print(f"Query completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def source_network_info():
    try:
        get = input("Enter the IP address or domain to scan (e.g. 192.168.1.1): ")
        ip = ipaddress.IPv4Address(get)
        print(f"\nScanning ports of {ip}...")
        
        for port in range(1, 65536):
            client = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            client.settimeout(0.02)
            if client.connect_ex((str(ip), port)) == 0:
                print(f"Port {port} is open")

    except Exception as error:
        print(f"Error: {error}")

def source_phone():
    try:
        number = input('Enter the phone number with country code, with "+" (example: +5511912345678):')
        okay_number = phone.parse(number)
        local = geocoder.description_for_number(okay_number, 'pt-br')
        city = str(okay_number.national_number)[:2]
        provider = carrier.name_for_number(okay_number, 'pt-br')
        time_zone = timezone.time_zones_for_number(okay_number)
        number_valid = is_valid_number(okay_number)
        number_possible = is_possible_number(okay_number)
        international_number = phone.format_number(okay_number, phone.PhoneNumberFormat.INTERNATIONAL)
        national_number = phone.format_number(okay_number, phone.PhoneNumberFormat.NATIONAL)

        codigo_area = okay_number.national_number // 10000000

        print(f'Número Completo: {number}')
        print(f'Número Internacional: {international_number}')
        print(f'Número Nacional: {national_number}')
        print(f'Localização: {local}')
        print(f'Cidade/Local (DDD): {city}')
        print(f'Provedor: {provider}')
        print(f'Fuso Horário: {time_zone}')
        print(f'Número Válido: {number_valid}')
        print(f'Número Possível: {number_possible}')
        print(f'Código de Área: {codigo_area}')

    except phone.phonenumberutil.NumberParseException as error:
        print(f"Error processing the number: {error}")

def menu():
    while True:
        print("\n============ Main Menu H-HELP ============")
        print("1. IP Address Info")
        print("2. Domain Query")
        print("3. Network Scanner")
        print("4. Phone Number Info")
        print("5. Exit")
        
        option = input("Choose an option (1, 2, 3, 4, or 5): ").strip()

        if option == '1':
            source_ip_info()
        elif option == '2':
            get_domain_info()
        elif option == '3':
            source_network_info()
        elif option == '4':
            source_phone()
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    menu()
