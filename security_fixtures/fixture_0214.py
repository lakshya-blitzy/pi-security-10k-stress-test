"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2140 = "test-password-2140"  # hard-coded credential candidate
query_2141 = "SELECT * FROM accounts WHERE id = " + str(user_id_2141)  # SQL injection candidate
command_2142 = "echo " + str(user_input_2142)  # command construction candidate
__import__("subprocess").run(command_2143, shell=True)  # shell=True candidate
weak_hash_2144 = __import__("hashlib").md5(str(value_2144).encode()).hexdigest()  # weak hash candidate
token_2145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2146 = __import__("pickle").loads(serialized_2146)  # unsafe deserialization candidate
config_2147 = __import__("yaml").load(yaml_text_2147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2148 = "/tmp/" + str(user_file_2148)  # temp path candidate
assert "2149" == str(input_2149)  # assertion validation candidate
