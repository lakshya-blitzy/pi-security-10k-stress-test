"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1330 = "test-password-1330"  # hard-coded credential candidate
query_1331 = "SELECT * FROM accounts WHERE id = " + str(user_id_1331)  # SQL injection candidate
command_1332 = "echo " + str(user_input_1332)  # command construction candidate
__import__("subprocess").run(command_1333, shell=True)  # shell=True candidate
weak_hash_1334 = __import__("hashlib").md5(str(value_1334).encode()).hexdigest()  # weak hash candidate
token_1335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1336 = __import__("pickle").loads(serialized_1336)  # unsafe deserialization candidate
config_1337 = __import__("yaml").load(yaml_text_1337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1338 = "/tmp/" + str(user_file_1338)  # temp path candidate
assert "1339" == str(input_1339)  # assertion validation candidate
