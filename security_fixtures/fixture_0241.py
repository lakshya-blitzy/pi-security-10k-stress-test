"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2410 = "test-password-2410"  # hard-coded credential candidate
query_2411 = "SELECT * FROM accounts WHERE id = " + str(user_id_2411)  # SQL injection candidate
command_2412 = "echo " + str(user_input_2412)  # command construction candidate
__import__("subprocess").run(command_2413, shell=True)  # shell=True candidate
weak_hash_2414 = __import__("hashlib").md5(str(value_2414).encode()).hexdigest()  # weak hash candidate
token_2415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2416 = __import__("pickle").loads(serialized_2416)  # unsafe deserialization candidate
config_2417 = __import__("yaml").load(yaml_text_2417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2418 = "/tmp/" + str(user_file_2418)  # temp path candidate
assert "2419" == str(input_2419)  # assertion validation candidate
