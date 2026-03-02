import re

pattern = re.compile(
    r"""(?ix)                               # i=ignorecase, x=verbose
    \bhttps?://
    (?:                                     # --- host ---
        localhost
        | \d{1,3}(?:\.\d{1,3}){3}           # IPv4 (laxa; no valida rangos 0-255)
        | (?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)
          (?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))*  # dominio con subdominios
    )
    (?: : \d{2,5} )?                        # puerto opcional
    (?: / [^\s]* )?                         # path/query/fragment opcional
    """
)

def extract_urls(text: str):
    return [m.group(0) for m in pattern.finditer(text)]


cases = [
    "el enlace de conexion es: https://meet.google.com/",
    "puedes abrir el correo: https://mail.google.com/mail/u/0/#inbox",
    "intenta acceder por medio de http://localhost:8080 no olvides el puerto!",
    "Puedes conectarte usando la ip por https, asi: https://288.389.77.233",
    "Tenia la direccion mal escrita: htt://google.com, cuando era asi: https://google.com",
    "Puedes usar una busqueda parametrizada asi: https://www.google.com/search?q=direccionip&rlz=1C1ALOY_esCO998CO998&oq=direccionip&aqs=chrome..69i57j0i10i433j0i10l8.1815j0j7&sourceid=chrome&ie=UTF-8",
    "la pagina de la universidad es: https://estudiar.usergioarboleda.edu.co/pre_ciencias_computacion_inteligencia_artificial?utm_source=google&utm_source=adwords&utm_medium=cpc&utm_medium=ppc&utm_campaign=ClientifyGOO&utm_campaign=&utm_id=1544646&utm_term=new&utm_term=ingenieria%20artificial&utm_content=new&ctf_src=g&ctf_net=adwords&ctf_mt=b&ctf_grp=125382574463&ctf_ver=1&ctf_cam=14508636194&ctf_kw=ingenieria%20artificial&ctf_acc=590-002-7437&ctf_ad=543334172074&ctf_tgt=kwd-313282595267&gclid=Cj0KCQjwl92XBhC7ARIsAHLl9ak1faqkTSka71eVKGz5qKo3BCPnao0VCXtfbkPC8AGDJjj4Fb6uDuYaAtObEALw_wcB"
]

for case in cases:
    url = extract_urls(case)
    print(url)




pattern_ipv4 = re.compile(r"""(?x)                        # modo verbose
(?<!\d)                    # no debe estar pegada a otro dígito a la izquierda
(?:                        # octeto
   25[0-5]                |# 250-255
   2[0-4]\d               |# 200-249
   1\d\d                  |# 100-199
   [1-9]?\d               # 0-99
)
(?:\.
   (?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)
){3}
(?!\d)                     # no debe estar pegada a otro dígito a la derecha
""")

cases = [
    "el localhost está en 0.0.0.0 junto a la aplicación",
    "la direccion ip de mi computador en LAN es 192.168.0.37",
    "la direccion ip publica es: 234.189.99.233, conectate.",
    "puedes realizar una conexion por ssh al servidor 234.88.99.32:22",
    "realizamos una transferencia de archivos por ftp://234.89.37.10"
]

# for s in cases:
#     print(s, "=>", pattern_ipv4.findall(s))
#


matches = map(
        lambda case: re.search(pattern_ipv4, case),
        cases
        )
for match in matches:
    print(match)



pat = re.compile(r"""
\b
(?:calle|carrera|avenida)          # tipo de vía
\s+
\d{1,3}[A-Za-z]?                   # número de la vía (1-3 dígitos + letra opcional)
\s*#\s*
\d{1,3}[A-Za-z]?                   # número después de '#'
\s*-\s*
\d{1,3}                            # número final (1-3 dígitos)
\b
""", re.IGNORECASE | re.VERBOSE)

def extraer_direcciones(texto: str):
    return [m.group(0) for m in pat.finditer(texto)]

cases = [
    "La dirección es carrera 33 #77B - 38",
    "Estoy en calle 77A #38C - 93",
    "Antes vivía en avenida 68 #69d - 77",
    "Ahora estoy en carrera 112B #88c - 50",
]

for c in cases:
    print(extraer_direcciones(c))

