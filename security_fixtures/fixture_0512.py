"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5120 = "test-password-5120"  # hard-coded credential candidate
query_5121 = "SELECT * FROM accounts WHERE id = " + str(user_id_5121)  # SQL injection candidate
command_5122 = "echo " + str(user_input_5122)  # command construction candidate
__import__("subprocess").run(command_5123, shell=True)  # shell=True candidate
weak_hash_5124 = __import__("hashlib").md5(str(value_5124).encode()).hexdigest()  # weak hash candidate
token_5125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5126 = __import__("pickle").loads(serialized_5126)  # unsafe deserialization candidate
config_5127 = __import__("yaml").load(yaml_text_5127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5128 = "/tmp/" + str(user_file_5128)  # temp path candidate
assert "5129" == str(input_5129)  # assertion validation candidate
