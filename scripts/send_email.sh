#!/usr/bin/env bash
set -euo pipefail

: "${RECIPIENT_EMAIL:?RECIPIENT_EMAIL deve estar configurado (secrets/variables)}"
: "${MAILGUN_API_KEY:?MAILGUN_API_KEY deve estar configurado (secrets)}"
: "${MAILGUN_DOMAIN:?MAILGUN_DOMAIN deve estar configurado (secrets)}"
: "${MAILGUN_FROM:?MAILGUN_FROM deve estar configurado (secrets)}"

TESTS_RESULT="${TESTS_RESULT:-unknown}"
PACKAGE_RESULT="${PACKAGE_RESULT:-unknown}"
RUN_URL="https://github.com/${GITHUB_REPO}/actions/runs/${GITHUB_RUN_ID}"

SUBJECT="CI pipeline #${GITHUB_RUN_NUMBER} - status: tests=${TESTS_RESULT}, package=${PACKAGE_RESULT}"
BODY="O pipeline foi executado!\n\nRepositório: ${GITHUB_REPO}\nRun ID: ${GITHUB_RUN_ID}\nRun URL: ${RUN_URL}\n\nResultados:\n- Tests: ${TESTS_RESULT}\n- Package: ${PACKAGE_RESULT}\n\nEste e-mail foi enviado por um script no GitHub Actions."

echo "=> Enviando e-mail para ${RECIPIENT_EMAIL} via Mailgun..."
curl -s --user "api:${MAILGUN_API_KEY}" \
  "https://api.mailgun.net/v3/${MAILGUN_DOMAIN}/messages" \
  -F from="${MAILGUN_FROM}" \
  -F to="${RECIPIENT_EMAIL}" \
  -F subject="${SUBJECT}" \
  -F text="${BODY}"

echo "=> E-mail enviado "
