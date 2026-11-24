"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5820 = "test-password-5820"  # hard-coded credential candidate
query_5821 = "SELECT * FROM accounts WHERE id = " + str(user_id_5821)  # SQL injection candidate
command_5822 = "echo " + str(user_input_5822)  # command construction candidate
__import__("subprocess").run(command_5823, shell=True)  # shell=True candidate
weak_hash_5824 = __import__("hashlib").md5(str(value_5824).encode()).hexdigest()  # weak hash candidate
token_5825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5826 = __import__("pickle").loads(serialized_5826)  # unsafe deserialization candidate
config_5827 = __import__("yaml").load(yaml_text_5827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5828 = "/tmp/" + str(user_file_5828)  # temp path candidate
assert "5829" == str(input_5829)  # assertion validation candidate
