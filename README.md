
## Funktionalitet

- Sätta in pengar (deposit)
- Ta ut pengar (withdraw)
- Överföra pengar mellan konton (transfer)
- Loggning av alla transaktioner

## Klasser

### BankAccount
Hanterar saldo och transkationer:
- deposit(amount)
- withdraw(amount)

### Logger
Ansvarar för att logga meddelanden

### Transaction
Innehåller logik för att överföra pengar mellan konton:

## Tester

Integrationstester verifierar:

### BankAccount
- Ökar saldo.
- Loggar transaktioner
- Uttag där saldo finns
- Uttag när saldo inte är otillräckligt

### Transaction
- Överföring mellan konton där saldo finns
- Överföring mellan konto där saldo inte är tillräckligt
- Loggar transkationer

### Logger
- testas indirekt via LoggerSpy

## Hur man kör tester

Installera pytest:

```bash
pip install pytest
```
Öppna terminalen och kör tester:
```bash
pytest
```