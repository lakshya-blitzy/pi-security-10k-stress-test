"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2380 = "test-password-2380"  # hard-coded credential candidate
query_2381 = "SELECT * FROM accounts WHERE id = " + str(user_id_2381)  # SQL injection candidate
command_2382 = "echo " + str(user_input_2382)  # command construction candidate
__import__("subprocess").run(command_2383, shell=True)  # shell=True candidate
weak_hash_2384 = __import__("hashlib").md5(str(value_2384).encode()).hexdigest()  # weak hash candidate
token_2385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2386 = __import__("pickle").loads(serialized_2386)  # unsafe deserialization candidate
config_2387 = __import__("yaml").load(yaml_text_2387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2388 = "/tmp/" + str(user_file_2388)  # temp path candidate
assert "2389" == str(input_2389)  # assertion validation candidate
