# SSH Deploy Key instellen op de server

Voer onderstaande commando's uit na het inloggen via:

```
ssh -p 7685 vannifr@vannifr.ovh
```

______________________________________________________________________

## Stap 1 — SSH directory aanmaken

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
```

## Stap 2 — Public key toevoegen

```bash
cat >> ~/.ssh/authorized_keys << 'EOF'
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8Q1SVbu18jqGN+mY5jYwlccD7Zl1/GxY15uG0qH4nzIb7P5Cj/Wi+P0Yflq+O9fkXVAkPw/fhLFc/6ZmQt1scnXLMxJxJeiYDecVrclEX3e985jYWavaCI0zdjtsVapZ2zg5zblykFft6PbfUuhdBuGOxvWB+qfW/pvFQ+TlkQSApmczZhgV1D4g3tMk5/tUTzrNz+X/UWPK8b1iXVAH5QbpQhp/1aVj9yuQtyldQp4MYSqdjVW6gIevkITZW3wQEjG74MsESj7TgeCLjdJFQ1YiIuDnj9LZSv2vNX3nvvEoFVqACjlhGgF7syvwofh1ROj0zijcZnso2lwDEzi8Sg2eGCY42KbiwlFIzzRYTNVz2tvAT6sjHdCJGeBoKSdjOvhW7IezhgfSmWnuOytzWDKCMX6zAwspuy+SsGe22+/6St71POp0h/WbZuMzaXiQ31NiStW2Mj9+4Lh+O+RTbrbCUBqx8XdT4Hogq7SMHVh3y8BJ1STv+JJYULljcLgFsR1XEvsPbHXQAFt1NllpKVJv/NXvgrkGRBVO5eHtvWdkdP3REQH8Yc25Wik2WlAWdefNRoQ8jCITmtt8YOmhhkimddFEitciItdS7U0IhVxhxOUaol4tkswqyC/aVMHfMKeDtFNs2wZY4XzpP5EeEEFDNcq3gDO1FHX3pZBT0dw== github-actions-deploy@ai-project-blueprint
EOF
```

## Stap 3 — Rechten instellen

```bash
chmod 600 ~/.ssh/authorized_keys
```

## Stap 4 — Controleer het pad voor de website

```bash
pwd
ls ~/public_html/
```

Stuur de output terug zodat het SSH_PATH secret correct ingesteld kan worden.

## Stap 5 — Verificatie (optioneel)

```bash
cat ~/.ssh/authorized_keys | tail -1
```

Verwachte output begint met: `ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8Q1...`
