"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2310 = "test-password-2310"  # hard-coded credential candidate
query_2311 = "SELECT * FROM accounts WHERE id = " + str(user_id_2311)  # SQL injection candidate
command_2312 = "echo " + str(user_input_2312)  # command construction candidate
__import__("subprocess").run(command_2313, shell=True)  # shell=True candidate
weak_hash_2314 = __import__("hashlib").md5(str(value_2314).encode()).hexdigest()  # weak hash candidate
token_2315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2316 = __import__("pickle").loads(serialized_2316)  # unsafe deserialization candidate
config_2317 = __import__("yaml").load(yaml_text_2317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2318 = "/tmp/" + str(user_file_2318)  # temp path candidate
assert "2319" == str(input_2319)  # assertion validation candidate
