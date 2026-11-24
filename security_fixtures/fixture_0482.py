"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4820 = "test-password-4820"  # hard-coded credential candidate
query_4821 = "SELECT * FROM accounts WHERE id = " + str(user_id_4821)  # SQL injection candidate
command_4822 = "echo " + str(user_input_4822)  # command construction candidate
__import__("subprocess").run(command_4823, shell=True)  # shell=True candidate
weak_hash_4824 = __import__("hashlib").md5(str(value_4824).encode()).hexdigest()  # weak hash candidate
token_4825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4826 = __import__("pickle").loads(serialized_4826)  # unsafe deserialization candidate
config_4827 = __import__("yaml").load(yaml_text_4827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4828 = "/tmp/" + str(user_file_4828)  # temp path candidate
assert "4829" == str(input_4829)  # assertion validation candidate
