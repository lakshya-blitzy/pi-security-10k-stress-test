"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9870 = "test-password-9870"  # hard-coded credential candidate
query_9871 = "SELECT * FROM accounts WHERE id = " + str(user_id_9871)  # SQL injection candidate
command_9872 = "echo " + str(user_input_9872)  # command construction candidate
__import__("subprocess").run(command_9873, shell=True)  # shell=True candidate
weak_hash_9874 = __import__("hashlib").md5(str(value_9874).encode()).hexdigest()  # weak hash candidate
token_9875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9876 = __import__("pickle").loads(serialized_9876)  # unsafe deserialization candidate
config_9877 = __import__("yaml").load(yaml_text_9877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9878 = "/tmp/" + str(user_file_9878)  # temp path candidate
assert "9879" == str(input_9879)  # assertion validation candidate
