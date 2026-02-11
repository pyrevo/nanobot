---
name: trading
description: Analisi di mercato crypto e trading journal. Usa quando l'utente chiede prezzi, analisi di mercato, trend crypto, supporti/resistenze, o vuole scrivere nel trading journal. Supporta BTC, ETH e altcoin principali via API gratuite.
---

# Trading

Skill per analisi di mercato e trading journal.

## Ottenere Prezzi in Tempo Reale

### CoinGecko (gratuito, no API key)

Prezzo singolo:
```bash
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,eur" | python3 -m json.tool
```

Top 10 per market cap:
```bash
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false" | python3 -c "
import json,sys
data=json.load(sys.stdin)
print(f'{'Coin':<15} {'Prezzo':>12} {'24h %':>8} {'MCap':>15}')
print('-'*52)
for c in data:
    print(f'{c[\"symbol\"].upper():<15} ${c[\"current_price\"]:>11,.2f} {c[\"price_change_percentage_24h\"]:>7.1f}% ${c[\"market_cap\"]:>13,.0f}')
"
```

Dati storici (ultimi 30 giorni):
```bash
curl -s "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30" | python3 -c "
import json,sys
data=json.load(sys.stdin)
prices=[p[1] for p in data['prices']]
print(f'Min 30d: ${min(prices):,.2f}')
print(f'Max 30d: ${max(prices):,.2f}')
print(f'Attuale: ${prices[-1]:,.2f}')
"
```

### Fear & Greed Index
```bash
curl -s "https://api.alternative.me/fng/?limit=1" | python3 -c "
import json,sys
d=json.load(sys.stdin)['data'][0]
print(f'Fear & Greed Index: {d[\"value\"]} ({d[\"value_classification\"]})')
"
```

## Framework di Analisi

Quando analizzi un mercato, segui questo framework:

1. **Contesto Macro**: Trend generale del mercato, BTC dominance, Fear & Greed
2. **Struttura di Mercato**: Higher highs/lows o lower highs/lows? Trend in atto?
3. **Livelli Chiave**: Supporti e resistenze significativi
4. **Bias**: Long, short, o neutro? Con che confidenza (alta/media/bassa)?
5. **Piano**: Cosa fare? Entry, stop loss, target. O stare fermi?

## Trading Journal

Dopo ogni analisi significativa, scrivi un journal entry in `memory/` con questo formato:

```markdown
## Trading Journal — [Data]

### Analisi [Coin]
- **Contesto**: ...
- **Livelli chiave**: S: $... R: $...
- **Bias**: Long/Short/Neutro (confidenza: alta/media/bassa)
- **Piano**: ...

### Operazioni
- (nessuna operazione / dettagli trade)

### Lezioni
- Cosa ho imparato oggi
```

## Regole di Sicurezza

- **MAI eseguire trade automatici** — solo analisi e suggerimenti
- Cita sempre la fonte dei dati (CoinGecko, Alternative.me, ecc.)
- Distingui sempre tra fatto e opinione
- Se non hai dati aggiornati, dillo chiaramente
