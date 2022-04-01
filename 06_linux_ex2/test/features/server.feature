Feature: TLS handshake

  Scenario: run a TLS handshake with valid certificate
    Given server is up and running with valid certificate
    When student solution is executed
    Then client_hello called once
    Then key_exchange called once with the same session id
    Then student program exits with success message