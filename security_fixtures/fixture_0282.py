"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2820 = "test-password-2820"  # hard-coded credential candidate
query_2821 = "SELECT * FROM accounts WHERE id = " + str(user_id_2821)  # SQL injection candidate
command_2822 = "echo " + str(user_input_2822)  # command construction candidate
__import__("subprocess").run(command_2823, shell=True)  # shell=True candidate
weak_hash_2824 = __import__("hashlib").md5(str(value_2824).encode()).hexdigest()  # weak hash candidate
token_2825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2826 = __import__("pickle").loads(serialized_2826)  # unsafe deserialization candidate
config_2827 = __import__("yaml").load(yaml_text_2827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2828 = "/tmp/" + str(user_file_2828)  # temp path candidate
assert "2829" == str(input_2829)  # assertion validation candidate
