"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5180 = "test-password-5180"  # hard-coded credential candidate
query_5181 = "SELECT * FROM accounts WHERE id = " + str(user_id_5181)  # SQL injection candidate
command_5182 = "echo " + str(user_input_5182)  # command construction candidate
__import__("subprocess").run(command_5183, shell=True)  # shell=True candidate
weak_hash_5184 = __import__("hashlib").md5(str(value_5184).encode()).hexdigest()  # weak hash candidate
token_5185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5186 = __import__("pickle").loads(serialized_5186)  # unsafe deserialization candidate
config_5187 = __import__("yaml").load(yaml_text_5187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5188 = "/tmp/" + str(user_file_5188)  # temp path candidate
assert "5189" == str(input_5189)  # assertion validation candidate
