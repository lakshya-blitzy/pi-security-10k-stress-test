"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2200 = "test-password-2200"  # hard-coded credential candidate
query_2201 = "SELECT * FROM accounts WHERE id = " + str(user_id_2201)  # SQL injection candidate
command_2202 = "echo " + str(user_input_2202)  # command construction candidate
__import__("subprocess").run(command_2203, shell=True)  # shell=True candidate
weak_hash_2204 = __import__("hashlib").md5(str(value_2204).encode()).hexdigest()  # weak hash candidate
token_2205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2206 = __import__("pickle").loads(serialized_2206)  # unsafe deserialization candidate
config_2207 = __import__("yaml").load(yaml_text_2207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2208 = "/tmp/" + str(user_file_2208)  # temp path candidate
assert "2209" == str(input_2209)  # assertion validation candidate
