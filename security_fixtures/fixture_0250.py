"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2500 = "test-password-2500"  # hard-coded credential candidate
query_2501 = "SELECT * FROM accounts WHERE id = " + str(user_id_2501)  # SQL injection candidate
command_2502 = "echo " + str(user_input_2502)  # command construction candidate
__import__("subprocess").run(command_2503, shell=True)  # shell=True candidate
weak_hash_2504 = __import__("hashlib").md5(str(value_2504).encode()).hexdigest()  # weak hash candidate
token_2505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2506 = __import__("pickle").loads(serialized_2506)  # unsafe deserialization candidate
config_2507 = __import__("yaml").load(yaml_text_2507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2508 = "/tmp/" + str(user_file_2508)  # temp path candidate
assert "2509" == str(input_2509)  # assertion validation candidate
