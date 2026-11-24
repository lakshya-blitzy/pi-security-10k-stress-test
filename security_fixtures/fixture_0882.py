"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8820 = "test-password-8820"  # hard-coded credential candidate
query_8821 = "SELECT * FROM accounts WHERE id = " + str(user_id_8821)  # SQL injection candidate
command_8822 = "echo " + str(user_input_8822)  # command construction candidate
__import__("subprocess").run(command_8823, shell=True)  # shell=True candidate
weak_hash_8824 = __import__("hashlib").md5(str(value_8824).encode()).hexdigest()  # weak hash candidate
token_8825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8826 = __import__("pickle").loads(serialized_8826)  # unsafe deserialization candidate
config_8827 = __import__("yaml").load(yaml_text_8827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8828 = "/tmp/" + str(user_file_8828)  # temp path candidate
assert "8829" == str(input_8829)  # assertion validation candidate
