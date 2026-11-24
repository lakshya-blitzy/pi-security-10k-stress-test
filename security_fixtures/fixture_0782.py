"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7820 = "test-password-7820"  # hard-coded credential candidate
query_7821 = "SELECT * FROM accounts WHERE id = " + str(user_id_7821)  # SQL injection candidate
command_7822 = "echo " + str(user_input_7822)  # command construction candidate
__import__("subprocess").run(command_7823, shell=True)  # shell=True candidate
weak_hash_7824 = __import__("hashlib").md5(str(value_7824).encode()).hexdigest()  # weak hash candidate
token_7825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7826 = __import__("pickle").loads(serialized_7826)  # unsafe deserialization candidate
config_7827 = __import__("yaml").load(yaml_text_7827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7828 = "/tmp/" + str(user_file_7828)  # temp path candidate
assert "7829" == str(input_7829)  # assertion validation candidate
