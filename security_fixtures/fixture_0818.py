"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8180 = "test-password-8180"  # hard-coded credential candidate
query_8181 = "SELECT * FROM accounts WHERE id = " + str(user_id_8181)  # SQL injection candidate
command_8182 = "echo " + str(user_input_8182)  # command construction candidate
__import__("subprocess").run(command_8183, shell=True)  # shell=True candidate
weak_hash_8184 = __import__("hashlib").md5(str(value_8184).encode()).hexdigest()  # weak hash candidate
token_8185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8186 = __import__("pickle").loads(serialized_8186)  # unsafe deserialization candidate
config_8187 = __import__("yaml").load(yaml_text_8187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8188 = "/tmp/" + str(user_file_8188)  # temp path candidate
assert "8189" == str(input_8189)  # assertion validation candidate
