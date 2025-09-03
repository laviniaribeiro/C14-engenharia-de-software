import unittest
from unittest.mock import patch, Mock
from main import obter  

class TestObterPiada(unittest.TestCase):

    # -------- 10 CASOS POSITIVOS --------
    @patch('main.requests.get')
    def test_piada_retorna_string(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris contou até infinito.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIsInstance(resultado, str)

    @patch('main.requests.get')
    def test_piada_nao_vazia(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Piada engraçada'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertTrue(len(resultado) > 0)

    @patch('main.requests.get')
    def test_piada_com_caracteres_especiais(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris 🥋 é invencível!'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIn('Chuck Norris', resultado)

    @patch('main.requests.get')
    def test_piada_com_numero(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris 1 x 0 qualquer adversário.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIn('1', resultado)

    @patch('main.requests.get')
    def test_piada_com_maiusculas(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'CHUCK NORRIS NÃO FALHA.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertTrue(resultado.isupper())

    @patch('main.requests.get')
    def test_piada_com_minusculas(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'chuck norris é lendário.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertTrue(resultado.islower())

    @patch('main.requests.get')
    def test_piada_com_espaco(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris pula corda.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIn(' ', resultado)

    @patch('main.requests.get')
    def test_piada_com_ponto_final(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris vence sem lutar.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertTrue(resultado.endswith('.'))

    @patch('main.requests.get')
    def test_piada_contendo_chuck(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Chuck Norris é imbatível.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIn('Chuck', resultado)

    @patch('main.requests.get')
    def test_piada_contendo_norris(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'Norris derrota qualquer inimigo.'}
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertIn('Norris', resultado)

    # -------- 10 CASOS NEGATIVOS --------
    @patch('main.requests.get')
    def test_erro_404(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

    @patch('main.requests.get')
    def test_erro_500(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

    @patch('main.requests.get')
    def test_json_invalido(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("JSON inválido")
        mock_get.return_value = mock_response
        with self.assertRaises(ValueError):
            obter()

    @patch('main.requests.get')
    def test_campo_value_faltando(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        with self.assertRaises(KeyError):
            obter()

    @patch('main.requests.get')
    def test_conexao_erro(self, mock_get):
        mock_get.side_effect = Exception("Falha de conexão")
        with self.assertRaises(Exception):
            obter()

    @patch('main.requests.get')
    def test_timeout(self, mock_get):
        mock_get.side_effect = TimeoutError("Timeout")
        with self.assertRaises(TimeoutError):
            obter()

    @patch('main.requests.get')
    def test_status_negativo_401(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

    @patch('main.requests.get')
    def test_status_negativo_403(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 403
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

    @patch('main.requests.get')
    def test_status_negativo_400(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

    @patch('main.requests.get')
    def test_status_negativo_503(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 503
        mock_get.return_value = mock_response
        resultado = obter()
        self.assertEqual(resultado, "Erro ao buscar piada.")

if __name__ == '__main__':
    unittest.main()
