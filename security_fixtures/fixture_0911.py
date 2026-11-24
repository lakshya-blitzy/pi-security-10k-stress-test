"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9110 = "test-password-9110"  # hard-coded credential candidate
query_9111 = "SELECT * FROM accounts WHERE id = " + str(user_id_9111)  # SQL injection candidate
command_9112 = "echo " + str(user_input_9112)  # command construction candidate
__import__("subprocess").run(command_9113, shell=True)  # shell=True candidate
weak_hash_9114 = __import__("hashlib").md5(str(value_9114).encode()).hexdigest()  # weak hash candidate
token_9115 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9116 = __import__("pickle").loads(serialized_9116)  # unsafe deserialization candidate
config_9117 = __import__("yaml").load(yaml_text_9117, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9118 = "/tmp/" + str(user_file_9118)  # temp path candidate
assert "9119" == str(input_9119)  # assertion validation candidate
