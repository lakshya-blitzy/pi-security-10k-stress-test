"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5090 = "test-password-5090"  # hard-coded credential candidate
query_5091 = "SELECT * FROM accounts WHERE id = " + str(user_id_5091)  # SQL injection candidate
command_5092 = "echo " + str(user_input_5092)  # command construction candidate
__import__("subprocess").run(command_5093, shell=True)  # shell=True candidate
weak_hash_5094 = __import__("hashlib").md5(str(value_5094).encode()).hexdigest()  # weak hash candidate
token_5095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5096 = __import__("pickle").loads(serialized_5096)  # unsafe deserialization candidate
config_5097 = __import__("yaml").load(yaml_text_5097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5098 = "/tmp/" + str(user_file_5098)  # temp path candidate
assert "5099" == str(input_5099)  # assertion validation candidate
