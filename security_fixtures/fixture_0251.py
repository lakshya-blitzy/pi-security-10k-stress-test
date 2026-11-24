"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2510 = "test-password-2510"  # hard-coded credential candidate
query_2511 = "SELECT * FROM accounts WHERE id = " + str(user_id_2511)  # SQL injection candidate
command_2512 = "echo " + str(user_input_2512)  # command construction candidate
__import__("subprocess").run(command_2513, shell=True)  # shell=True candidate
weak_hash_2514 = __import__("hashlib").md5(str(value_2514).encode()).hexdigest()  # weak hash candidate
token_2515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2516 = __import__("pickle").loads(serialized_2516)  # unsafe deserialization candidate
config_2517 = __import__("yaml").load(yaml_text_2517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2518 = "/tmp/" + str(user_file_2518)  # temp path candidate
assert "2519" == str(input_2519)  # assertion validation candidate
