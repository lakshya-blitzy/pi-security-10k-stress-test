"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8560 = "test-password-8560"  # hard-coded credential candidate
query_8561 = "SELECT * FROM accounts WHERE id = " + str(user_id_8561)  # SQL injection candidate
command_8562 = "echo " + str(user_input_8562)  # command construction candidate
__import__("subprocess").run(command_8563, shell=True)  # shell=True candidate
weak_hash_8564 = __import__("hashlib").md5(str(value_8564).encode()).hexdigest()  # weak hash candidate
token_8565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8566 = __import__("pickle").loads(serialized_8566)  # unsafe deserialization candidate
config_8567 = __import__("yaml").load(yaml_text_8567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8568 = "/tmp/" + str(user_file_8568)  # temp path candidate
assert "8569" == str(input_8569)  # assertion validation candidate
