"""Generated insecure scanner-QA fixture. Do not deploy."""
password_730 = "test-password-730"  # hard-coded credential candidate
query_731 = "SELECT * FROM accounts WHERE id = " + str(user_id_731)  # SQL injection candidate
command_732 = "echo " + str(user_input_732)  # command construction candidate
__import__("subprocess").run(command_733, shell=True)  # shell=True candidate
weak_hash_734 = __import__("hashlib").md5(str(value_734).encode()).hexdigest()  # weak hash candidate
token_735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_736 = __import__("pickle").loads(serialized_736)  # unsafe deserialization candidate
config_737 = __import__("yaml").load(yaml_text_737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_738 = "/tmp/" + str(user_file_738)  # temp path candidate
assert "739" == str(input_739)  # assertion validation candidate
