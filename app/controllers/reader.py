from models.language import Language
from models.production import Production
from models.pattern import Pattern
from models.token import Token
from data.constants import (
    JSON_URL, TXT_URL, REGEX, UTF8, ARROW, PIPE, SPACE
)
import json
import re


class Reader:
    ''' Class Reader is used to read files. '''

    def __init__(self, txt_url: str = TXT_URL, json_url: str = JSON_URL) -> None:
        self._json_url: str = json_url
        self._txt_url: str = txt_url

    def str_to_lang(self, string: str = "") -> Language:
        ''' Read txt file and return a language. '''

        lang_title: str = ''
        lang_prods: list[Production] = []

        lines = string.splitlines()

        for idx, linea in enumerate(lines):
            if idx == 0:
                lang_title: str = linea.split(':')[-1].strip()
                continue

            prod_patterns: list[Pattern] = []

            # print(f'\n{idx}: {linea}')

            mlexema: str = linea.split(ARROW)[0].strip()
            is_mtk_variable: bool = self.is_variable(mlexema)
            token: Token = Token(
                mlexema,
                not is_mtk_variable
            )

            patterns_0fn: str = linea.split(ARROW)[-1].strip()
            new_patterns: list[str] = [
                pattern.strip()
                for pattern in patterns_0fn.split(PIPE)
            ]
            # print(f'new patterns: {new_patterns}')

            for pattern in new_patterns:

                lexemas: list[str] = pattern.split(SPACE)
                # print(f'lexemas: {lexemas}')
                stokens: list[Token] = []

                for lexema in lexemas:
                    is_variable_tk: bool = self.is_variable(lexema)
                    pattern_token: Token = Token(
                        lexema,
                        not is_variable_tk
                    )
                    stokens.append(pattern_token)

                new_pattern: Pattern = Pattern(stokens)
                prod_patterns.append(new_pattern)

                # print('pattern new:', new_pattern)

            new_production: Production = Production(token, prod_patterns)
            lang_prods.append(new_production)

        new_language: Language = Language(lang_title, lang_prods)

        return new_language
    
    def txt_to_lang(self, url_file: str = TXT_URL) -> Language:
        ''' Read txt file and return a language. '''
        if url_file is not None:
            self._txt_url = url_file

        lang_title: str = ''
        lang_prods: list[Production] = []

        with open(self._txt_url, 'r', encoding=UTF8) as archivo:
            lines = archivo.readlines()

            for idx, linea in enumerate(lines):
                if idx == 0:
                    lang_title: str = linea.split(':')[-1].strip()
                    continue

                prod_patterns: list[Pattern] = []

                # print(f'\n{idx}: {linea}')

                mlexema: str = linea.split(ARROW)[0].strip()
                is_mtk_variable: bool = self.is_variable(mlexema)
                token: Token = Token(
                    mlexema,
                    not is_mtk_variable
                )

                patterns_0fn: str = linea.split(ARROW)[-1].strip()
                new_patterns: list[str] = [
                    pattern.strip()
                    for pattern in patterns_0fn.split(PIPE)
                ]
                # print(f'new patterns: {new_patterns}')

                for pattern in new_patterns:

                    lexemas: list[str] = pattern.split(SPACE)
                    # print(f'lexemas: {lexemas}')
                    stokens: list[Token] = []

                    for lexema in lexemas:
                        is_variable_tk: bool = self.is_variable(lexema)
                        pattern_token: Token = Token(
                            lexema,
                            not is_variable_tk
                        )
                        stokens.append(pattern_token)

                    new_pattern: Pattern = Pattern(stokens)
                    prod_patterns.append(new_pattern)

                    # print('pattern new:', new_pattern)

                new_production: Production = Production(token, prod_patterns)
                lang_prods.append(new_production)

        new_language: Language = Language(lang_title, lang_prods)

        return new_language

    def json_to_language(self) -> Language:
        ''' Read json file and return a language. '''
        with open(self._json_url, encoding=UTF8) as json_file:
            data = json.load(json_file)

            language: Language = Language(
                name=data['language']['name'],
                productions=[
                    Production(
                        main_token=Token(
                            lexema=prod['token']['lexema'],
                            is_terminal=prod['token']['is_terminal']
                        ),
                        patterns=[
                            Pattern(
                                tokens=[
                                    Token(
                                        lexema=token['lexema'],
                                        is_terminal=token['is_terminal']
                                    )
                                    for token in pattern['tokens']
                                ]
                            )
                            for pattern in prod['patterns']
                        ]
                    )
                    for prod in data['language']['productions']
                ]
            )
        return language

    def is_variable(self, lexema: str) -> bool:
        ''' Function to detect if lexema is a variable. '''
        return bool(re.match(REGEX, lexema))
