"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2230 = "test-password-2230"  # hard-coded credential candidate
query_2231 = "SELECT * FROM accounts WHERE id = " + str(user_id_2231)  # SQL injection candidate
command_2232 = "echo " + str(user_input_2232)  # command construction candidate
__import__("subprocess").run(command_2233, shell=True)  # shell=True candidate
weak_hash_2234 = __import__("hashlib").md5(str(value_2234).encode()).hexdigest()  # weak hash candidate
token_2235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2236 = __import__("pickle").loads(serialized_2236)  # unsafe deserialization candidate
config_2237 = __import__("yaml").load(yaml_text_2237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2238 = "/tmp/" + str(user_file_2238)  # temp path candidate
assert "2239" == str(input_2239)  # assertion validation candidate
