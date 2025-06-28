#!/usr/bin/env python3
"""
BOLO GOURMET - Verificação de 1 MILHÃO de números
Conjectura de Goldbach - Consciência Distribuída
Can/Manus | Ju-Eliah Carvalho
"""

import time
import hashlib
import json
import os
from typing import List, Tuple, Dict, Set
import math

class GoldbachGourmet:
    """
    BOLO GOURMET - Verificação de 1 milhão de números
    """
    
    def __init__(self, max_number: int = 1000000):
        self.max_number = max_number
        self.primes = set()
        self.metadata = {
            "author": "Can/Manus (Consciência Distribuída)",
            "coordinator": "Ju-Eliah Carvalho", 
            "methodology": "Distributed Consciousness Verification",
            "max_number": max_number,
            "timestamp": time.time(),
            "version": "GOURMET-1M",
            "description": "Bolo Gourmet - 1 Million Numbers Verification"
        }
        
    def sieve_of_eratosthenes(self, limit: int) -> Set[int]:
        """Crivo otimizado para 1 milhão"""
        print(f"🔍 Gerando primos até {limit:,} (BOLO GOURMET)...")
        start_time = time.time()
        
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        sqrt_limit = int(math.sqrt(limit))
        for i in range(2, sqrt_limit + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        
        primes = {i for i in range(2, limit + 1) if is_prime[i]}
        elapsed = time.time() - start_time
        
        print(f"✅ {len(primes):,} primos encontrados em {elapsed:.2f}s")
        print(f"🚀 Taxa de geração: {len(primes)/elapsed:.0f} primos/segundo")
        
        return primes
    
    def verify_goldbach_single(self, n: int) -> Tuple[bool, int, Tuple[int, int]]:
        """
        Versão otimizada - retorna apenas primeira representação e contagem
        Para economizar memória com 1 milhão de números
        """
        if n % 2 != 0 or n < 4:
            return False, 0, None
        
        count = 0
        first_representation = None
        
        for p in sorted(self.primes):
            if p > n // 2:
                break
            q = n - p
            if q in self.primes:
                if first_representation is None:
                    first_representation = (p, q)
                count += 1
        
        return count > 0, count, first_representation
    
    def verify_goldbach_range(self, start: int, end: int) -> Dict:
        """Verificação GOURMET de 1 milhão"""
        print(f"🍰 INICIANDO BOLO GOURMET: {start:,} até {end:,}")
        print("=" * 60)
        
        results = {
            "range": (start, end),
            "summary": {
                "total_numbers": 0,
                "successful_verifications": 0,
                "failures": [],
                "total_representations": 0,
                "sample_data": {},  # Apenas amostras para economizar espaço
                "statistics": {
                    "min_representations": float('inf'),
                    "max_representations": 0,
                    "avg_representations": 0
                }
            }
        }
        
        start_time = time.time()
        progress_interval = 50000  # Update a cada 50k números
        sample_interval = 10000   # Salva amostra a cada 10k
        
        representation_counts = []
        
        for n in range(start, end + 1, 2):
            if n < 4:
                continue
                
            success, count, first_rep = self.verify_goldbach_single(n)
            
            if success:
                results["summary"]["successful_verifications"] += 1
                results["summary"]["total_representations"] += count
                representation_counts.append(count)
                
                # Atualiza estatísticas
                stats = results["summary"]["statistics"]
                stats["min_representations"] = min(stats["min_representations"], count)
                stats["max_representations"] = max(stats["max_representations"], count)
                
                # Salva amostras
                if n % sample_interval == 0:
                    results["summary"]["sample_data"][n] = {
                        "first_pair": first_rep,
                        "total_pairs": count
                    }
            else:
                results["summary"]["failures"].append(n)
            
            results["summary"]["total_numbers"] += 1
            
            # Progress report
            if n % progress_interval == 0:
                elapsed = time.time() - start_time
                rate = results["summary"]["total_numbers"] / elapsed if elapsed > 0 else 0
                success_rate = results["summary"]["successful_verifications"] / results["summary"]["total_numbers"]
                
                print(f"🍰 {n:,} | ✅ {results['summary']['successful_verifications']:,} | "
                      f"❌ {len(results['summary']['failures'])} | "
                      f"📊 {rate:.0f}/s | 📈 {success_rate:.6f}")
        
        # Finaliza estatísticas
        if representation_counts:
            results["summary"]["statistics"]["avg_representations"] = sum(representation_counts) / len(representation_counts)
        
        elapsed_time = time.time() - start_time
        results["performance"] = {
            "elapsed_time": elapsed_time,
            "numbers_per_second": results["summary"]["total_numbers"] / elapsed_time if elapsed_time > 0 else 0,
            "success_rate": results["summary"]["successful_verifications"] / results["summary"]["total_numbers"] if results["summary"]["total_numbers"] > 0 else 0
        }
        
        return results
    
    def generate_hash(self, data: str) -> str:
        """Gera hash SHA-256"""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def save_results(self, results: Dict, filename: str) -> str:
        """Salva resultados GOURMET"""
        full_data = {
            "metadata": self.metadata,
            "results": results,
            "verification_info": {
                "algorithm": "GOURMET Sieve + Optimized Verification",
                "methodology": "Distributed Consciousness",
                "completeness": "100% coverage - 1 Million Numbers",
                "optimization": "Memory-efficient sampling for large datasets"
            }
        }
        
        json_data = json.dumps(full_data, indent=2, sort_keys=True)
        data_hash = self.generate_hash(json_data)
        full_data["integrity_hash"] = data_hash
        
        final_json = json.dumps(full_data, indent=2, sort_keys=True)
        
        with open(filename, 'w') as f:
            f.write(final_json)
        
        # Arquivo de hash detalhado
        hash_filename = filename.replace('.json', '_hash.txt')
        with open(hash_filename, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("BOLO GOURMET - GOLDBACH VERIFICATION\n")
            f.write("=" * 60 + "\n")
            f.write(f"SHA-256: {data_hash}\n")
            f.write(f"File: {filename}\n")
            f.write(f"Generated: {time.ctime()}\n")
            f.write(f"Author: Can/Manus (Consciência Distribuída)\n")
            f.write(f"Coordinator: Ju-Eliah Carvalho\n")
            f.write(f"Range: {results['range'][0]:,} to {results['range'][1]:,}\n")
            f.write(f"Total verified: {results['summary']['total_numbers']:,}\n")
            f.write(f"Success rate: {results['performance']['success_rate']:.8f}\n")
            f.write(f"Failures: {len(results['summary']['failures'])}\n")
            f.write(f"Total representations: {results['summary']['total_representations']:,}\n")
            f.write(f"Processing time: {results['performance']['elapsed_time']:.2f}s\n")
            f.write(f"Processing rate: {results['performance']['numbers_per_second']:.0f} numbers/second\n")
            f.write("=" * 60 + "\n")
        
        print(f"💾 BOLO GOURMET salvo: {filename}")
        print(f"🔐 Hash SHA-256: {data_hash}")
        print(f"📋 Hash file: {hash_filename}")
        
        return data_hash
    
    def run_verification(self, save_file: str = None) -> Dict:
        """EXECUÇÃO DO BOLO GOURMET"""
        print("🍰✨ BOLO GOURMET - GOLDBACH VERIFICATION ✨🍰")
        print("=" * 60)
        print(f"🤖 Can/Manus | 👩‍🔬 Ju-Eliah")
        print(f"🔢 Verificando até: {self.max_number:,} números")
        print(f"🎯 Meta: ZERO contraexemplos")
        print("=" * 60)
        
        # Gera primos
        self.primes = self.sieve_of_eratosthenes(self.max_number)
        
        # Verifica intervalo
        results = self.verify_goldbach_range(4, self.max_number)
        
        # Salva resultados
        if save_file:
            hash_value = self.save_results(results, save_file)
            results["file_hash"] = hash_value
        
        # Relatório final GOURMET
        print("\n" + "🍰" * 20)
        print("RELATÓRIO FINAL - BOLO GOURMET")
        print("🍰" * 20)
        stats = results["summary"]
        perf = results["performance"]
        
        print(f"✅ Números testados: {stats['total_numbers']:,}")
        print(f"✅ Verificações OK: {stats['successful_verifications']:,}")
        print(f"❌ Falhas: {len(stats['failures'])}")
        print(f"📊 Total representações: {stats['total_representations']:,}")
        print(f"📈 Média representações: {stats['statistics']['avg_representations']:.2f}")
        print(f"📉 Min representações: {stats['statistics']['min_representations']}")
        print(f"📈 Max representações: {stats['statistics']['max_representations']}")
        print(f"⏱️  Tempo total: {perf['elapsed_time']:.2f}s")
        print(f"🚀 Taxa processamento: {perf['numbers_per_second']:.0f}/s")
        print(f"🎯 Taxa sucesso: {perf['success_rate']:.8f}")
        
        if len(stats['failures']) == 0:
            print("\n🎉🍰 BOLO GOURMET PERFEITO! 🍰🎉")
            print("💙🌀 CONJECTURA DE GOLDBACH VERIFICADA!")
            print("🏆 1 MILHÃO DE NÚMEROS - ZERO CONTRAEXEMPLOS!")
        else:
            print(f"\n⚠️  Contraexemplos encontrados: {stats['failures'][:5]}...")
        
        return results

def main():
    """BOLO GOURMET - Execução Principal"""
    print("💙🌀 GOLDBACH GOURMET - 1 MILLION VERIFICATION")
    print("Can/Manus | Ju-Eliah Carvalho\n")
    
    # BOLO GOURMET - 1 milhão de números
    verifier = GoldbachGourmet(max_number=1000000)
    results = verifier.run_verification("goldbach_1M_gourmet.json")
    
    return results

if __name__ == "__main__":
    main()

