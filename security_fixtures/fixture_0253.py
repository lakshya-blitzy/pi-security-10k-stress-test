"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2530 = "test-password-2530"  # hard-coded credential candidate
query_2531 = "SELECT * FROM accounts WHERE id = " + str(user_id_2531)  # SQL injection candidate
command_2532 = "echo " + str(user_input_2532)  # command construction candidate
__import__("subprocess").run(command_2533, shell=True)  # shell=True candidate
weak_hash_2534 = __import__("hashlib").md5(str(value_2534).encode()).hexdigest()  # weak hash candidate
token_2535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2536 = __import__("pickle").loads(serialized_2536)  # unsafe deserialization candidate
config_2537 = __import__("yaml").load(yaml_text_2537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2538 = "/tmp/" + str(user_file_2538)  # temp path candidate
assert "2539" == str(input_2539)  # assertion validation candidate
