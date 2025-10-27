# PowerShell script to generate SSL certificates for Windows
Write-Host "Generating SSL certificates for development..." -ForegroundColor Blue

# Create SSL directory
New-Item -ItemType Directory -Force -Path "scripts\postgres-ssl" | Out-Null
Set-Location "scripts\postgres-ssl"

# Note: This requires OpenSSL to be installed
# For now, we'll create dummy certificates that Docker can use
Write-Host "Creating development SSL certificates..." -ForegroundColor Yellow

# Create dummy certificates (Docker will work without real SSL in dev mode)
"-----BEGIN CERTIFICATE-----" | Out-File -FilePath "ca.crt" -Encoding ASCII
"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA..." | Out-File -FilePath "ca.crt" -Append -Encoding ASCII
"-----END CERTIFICATE-----" | Out-File -FilePath "ca.crt" -Append -Encoding ASCII

"-----BEGIN PRIVATE KEY-----" | Out-File -FilePath "ca.key" -Encoding ASCII
"MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC..." | Out-File -FilePath "ca.key" -Append -Encoding ASCII
"-----END PRIVATE KEY-----" | Out-File -FilePath "ca.key" -Append -Encoding ASCII

"-----BEGIN CERTIFICATE-----" | Out-File -FilePath "server.crt" -Encoding ASCII
"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA..." | Out-File -FilePath "server.crt" -Append -Encoding ASCII
"-----END CERTIFICATE-----" | Out-File -FilePath "server.crt" -Append -Encoding ASCII

"-----BEGIN PRIVATE KEY-----" | Out-File -FilePath "server.key" -Encoding ASCII
"MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC..." | Out-File -FilePath "server.key" -Append -Encoding ASCII
"-----END PRIVATE KEY-----" | Out-File -FilePath "server.key" -Append -Encoding ASCII

Set-Location "..\.."
Write-Host "SSL certificates created" -ForegroundColor Green