"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8250 = "test-password-8250"  # hard-coded credential candidate
query_8251 = "SELECT * FROM accounts WHERE id = " + str(user_id_8251)  # SQL injection candidate
command_8252 = "echo " + str(user_input_8252)  # command construction candidate
__import__("subprocess").run(command_8253, shell=True)  # shell=True candidate
weak_hash_8254 = __import__("hashlib").md5(str(value_8254).encode()).hexdigest()  # weak hash candidate
token_8255 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8256 = __import__("pickle").loads(serialized_8256)  # unsafe deserialization candidate
config_8257 = __import__("yaml").load(yaml_text_8257, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8258 = "/tmp/" + str(user_file_8258)  # temp path candidate
assert "8259" == str(input_8259)  # assertion validation candidate
