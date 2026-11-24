"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8510 = "test-password-8510"  # hard-coded credential candidate
query_8511 = "SELECT * FROM accounts WHERE id = " + str(user_id_8511)  # SQL injection candidate
command_8512 = "echo " + str(user_input_8512)  # command construction candidate
__import__("subprocess").run(command_8513, shell=True)  # shell=True candidate
weak_hash_8514 = __import__("hashlib").md5(str(value_8514).encode()).hexdigest()  # weak hash candidate
token_8515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8516 = __import__("pickle").loads(serialized_8516)  # unsafe deserialization candidate
config_8517 = __import__("yaml").load(yaml_text_8517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8518 = "/tmp/" + str(user_file_8518)  # temp path candidate
assert "8519" == str(input_8519)  # assertion validation candidate
